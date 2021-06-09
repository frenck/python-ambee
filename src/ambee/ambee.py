"""Asynchronous Python client for the Ambee API."""
from __future__ import annotations

import asyncio
import json
import socket
from dataclasses import dataclass
from typing import Any

import aiohttp
import async_timeout
from yarl import URL

from .exceptions import (
    AmbeeAuthenticationError,
    AmbeeConnectionError,
    AmbeeConnectionTimeoutError,
    AmbeeError,
)
from .models import AirQuality, Pollen, Weather


@dataclass
class Ambee:
    """Main class for handling connections with the Ambee API."""

    api_key: str
    latitude: float
    longitude: float
    request_timeout: float = 10.0
    session: aiohttp.client.ClientSession | None = None

    _close_session: bool = False

    async def request(
        self,
        uri: str = "",
    ) -> Any:
        """Handle a request to the Ambee API.

        A generic method for sending/handling HTTP requests done gainst
        the Ambee API.

        Args:
            uri: Request base URI, for example `weather`

        Returns:
            A Python dictionary (JSON decoded) with the response from the
            Ambee API.

        Raises:
            AmbeeConnectionError: An error occurred while communitcation with
                the Ambee API.
            AmbeeAuthenticationError: The API key provided is not valid.
            AmbeeConnectionTimeoutError: A timeout occurred while communicating
                with the Ambee API.
            AmbeeError: Received an unexpected response from the Ambee API.
        """
        url = URL.build(
            scheme="https", host="api.ambeedata.com", port=443, path=f"/{uri}/"
        ).join(URL("by-lat-lng"))

        if self.session is None:
            self.session = aiohttp.ClientSession()
            self._close_session = True

        try:
            with async_timeout.timeout(self.request_timeout):
                response = await self.session.request(
                    "GET",
                    url,
                    params={
                        "lat": self.latitude,
                        "lng": self.longitude,
                    },
                    headers={
                        "x-api-key": self.api_key,
                        "Accept": "application/json",
                    },
                )
        except asyncio.TimeoutError as exception:
            raise AmbeeConnectionTimeoutError(
                "Timeout occurred while connecting to the Ambee API"
            ) from exception
        except (aiohttp.ClientError, socket.gaierror) as exception:
            raise AmbeeConnectionError(
                "Error occurred while communicating with the Ambee API"
            ) from exception

        if response.status in {401, 403}:
            raise AmbeeAuthenticationError("The provided Ambee API key is not an valid")

        content_type = response.headers.get("Content-Type", "")
        if (response.status // 100) in {4, 5}:
            contents = await response.read()
            response.close()

            if content_type == "application/json":
                raise AmbeeError(response.status, json.loads(contents.decode("utf8")))
            raise AmbeeError(response.status, {"message": contents.decode("utf8")})

        if "application/json" not in content_type:
            text = await response.text()
            raise AmbeeError(
                "Unexpected response from Ambee API",
                {"message": text},
            )

        response_data = await response.json()

        if (
            "message" not in response_data
            or response_data["message"].lower() != "success"
        ):
            raise AmbeeError("Unexpected response from Ambee API", response_data)

        return response_data

    async def air_quality(self) -> AirQuality:
        """Get the latest, real-time hyper local air quality data.

        Ambee Air Quality API helps you to get real-time hyper local air quality
        data for over a million postal codes across 90+ countries, cities by
        latitude & longitude. Air quality data helps quantify ambient air
        pollution.

        Returns:
            A AirQuality data object for the configured coordinates.
        """
        data = await self.request("latest")
        return AirQuality.from_dict(data)

    async def pollen(self) -> Pollen:
        """Get the latest, real-time pollen count.

        Pollen is a fine powder produced by trees and plants. Pollen can
        severely affect people, especially those with different ailments such
        as asthma and respiratory issues. It can aggravate these existing
        conditions or cause these issues in high risk groups.

        Returns:
            A Pollen data object for the configured coordinates.
        """
        data = await self.request("latest/pollen")
        return Pollen.from_dict(data)

    async def weather(self) -> Weather:
        """Get the latest, real-time weather conditions.

        Ambee Weather API gives access to real-time local weather updates for
        temperature, pressure, humidity, wind, cloud coverage, visibility, and
        dew point of any location in the world.

        Returns:
            A Weather data object for the configured coordinates.
        """
        data = await self.request("weather/latest")
        return Weather.from_dict(data)

    async def close(self) -> None:
        """Close open client session."""
        if self.session and self._close_session:
            await self.session.close()

    async def __aenter__(self) -> Ambee:
        """Async enter.

        Returns:
            The Ambee object.
        """
        return self

    async def __aexit__(self, *_exc_info) -> None:
        """Async exit.

        Args:
            _exc_info: Exec type.
        """
        await self.close()
