"""Tests for `ambee.Ambee`."""
import asyncio
from unittest.mock import patch

import aiohttp
import pytest

from ambee import Ambee
from ambee.exceptions import AmbeeAuthenticationError, AmbeeConnectionError, AmbeeError


@pytest.mark.asyncio
async def test_json_request(aresponses):
    """Test JSON response is handled correctly."""
    aresponses.add(
        "api.ambeedata.com",
        "/latest/by-lat-lng",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text='{"message": "success"}',
        ),
    )
    async with aiohttp.ClientSession() as session:
        client = Ambee(api_key="example", latitude=12, longitude=77, session=session)
        response = await client.request()
        assert response["message"] == "success"
        await client.close()


@pytest.mark.asyncio
async def test_text_request(aresponses):
    """Test non JSON response is handled correctly."""
    aresponses.add(
        "api.ambeedata.com",
        "/latest/by-lat-lng",
        "GET",
        aresponses.Response(status=200, text="OK"),
    )
    async with aiohttp.ClientSession() as session:
        client = Ambee(api_key="example", latitude=12, longitude=77, session=session)
        with pytest.raises(AmbeeError):
            await client.request()


@pytest.mark.asyncio
async def test_internal_session(aresponses):
    """Test JSON response is handled correctly."""
    aresponses.add(
        "api.ambeedata.com",
        "/latest/by-lat-lng",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text='{"message": "success"}',
        ),
    )
    async with Ambee(api_key="example", latitude=12, longitude=77) as client:
        response = await client.request()
        assert response["message"] == "success"


@pytest.mark.asyncio
async def test_timeout(aresponses):
    """Test request timeout from Ambee API."""
    # Faking a timeout by sleeping
    async def response_handler(_):
        await asyncio.sleep(0.2)
        return aresponses.Response(body="Goodmorning!")

    aresponses.add("api.ambeedata.com", "/latest/by-lat-lng", "GET", response_handler)

    async with aiohttp.ClientSession() as session:
        client = Ambee(
            api_key="example",
            latitude=12,
            longitude=77,
            session=session,
            request_timeout=0.1,
        )
        with pytest.raises(AmbeeConnectionError):
            assert await client.request()


@pytest.mark.asyncio
async def test_client_error():
    """Test request client error from Ambee."""
    async with aiohttp.ClientSession() as session:
        client = Ambee(
            api_key="example",
            latitude=12,
            longitude=77,
            session=session,
        )
        with patch.object(
            session, "request", side_effect=aiohttp.ClientError
        ), pytest.raises(AmbeeConnectionError):
            assert await client.request()


@pytest.mark.asyncio
@pytest.mark.parametrize("status", [401, 403])
async def test_http_error401(aresponses, status):
    """Test HTTP 401 response handling."""
    aresponses.add(
        "api.ambeedata.com",
        "/latest/by-lat-lng",
        "GET",
        aresponses.Response(text="OMG PUPPIES!", status=status),
    )

    async with aiohttp.ClientSession() as session:
        client = Ambee(api_key="example", latitude=12, longitude=77, session=session)
        with pytest.raises(AmbeeAuthenticationError):
            assert await client.request()


@pytest.mark.asyncio
async def test_http_error400(aresponses):
    """Test HTTP 404 response handling."""
    aresponses.add(
        "api.ambeedata.com",
        "/latest/by-lat-lng",
        "GET",
        aresponses.Response(text="OMG PUPPIES!", status=404),
    )

    async with aiohttp.ClientSession() as session:
        client = Ambee(api_key="example", latitude=12, longitude=77, session=session)
        with pytest.raises(AmbeeError):
            assert await client.request()


@pytest.mark.asyncio
async def test_http_error500(aresponses):
    """Test HTTP 500 response handling."""
    aresponses.add(
        "api.ambeedata.com",
        "/latest/by-lat-lng",
        "GET",
        aresponses.Response(
            body=b'{"status":"nok"}',
            status=500,
            headers={"Content-Type": "application/json"},
        ),
    )

    async with aiohttp.ClientSession() as session:
        client = Ambee(api_key="example", latitude=12, longitude=77, session=session)
        with pytest.raises(AmbeeError):
            assert await client.request()


@pytest.mark.asyncio
async def test_no_success(aresponses):
    """Test a message without a success message throws."""
    aresponses.add(
        "api.ambeedata.com",
        "/latest/by-lat-lng",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text='{"message": "no success"}',
        ),
    )

    async with aiohttp.ClientSession() as session:
        client = Ambee(api_key="example", latitude=12, longitude=77, session=session)
        with pytest.raises(AmbeeError):
            assert await client.request()
