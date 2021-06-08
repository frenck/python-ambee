"""Models for Ambee."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class AirQuality:
    """Object representing an AirQuality response from Ambee."""

    particulate_matter_2_5: float | None
    particulate_matter_10: float | None
    sulphur_dioxide: float | None
    nitrogen_dioxide: float | None
    ozone: float | None
    carbon_monoxide: float | None
    air_quality_index: int | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> AirQuality:
        """Return AirQuality object from the Ambee API response.

        Args:
            data: The data from the Ambee API.

        Returns:
            A AirQuality object.
        """
        station = data["stations"][0]
        return AirQuality(
            particulate_matter_2_5=station.get("PM25"),
            particulate_matter_10=station.get("PM10"),
            sulphur_dioxide=station.get("SO2"),
            nitrogen_dioxide=station.get("NO2"),
            ozone=station.get("OZONE"),
            carbon_monoxide=station.get("CO"),
            air_quality_index=station.get("AQI"),
        )
