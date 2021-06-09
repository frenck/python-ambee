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


@dataclass
class Pollen:
    """Object representing an Pollen response from Ambee."""

    grass_poaceae: int | None
    grass_risk: str | None
    grass: int | None
    tree_alder: int | None
    tree_birch: int | None
    tree_cypress: int | None
    tree_elm: int | None
    tree_hazel: int | None
    tree_oak: int | None
    tree_pine: int | None
    tree_plane: int | None
    tree_poplar: int | None
    tree_risk: str | None
    tree: int | None
    weed_chenopod: int | None
    weed_mugwort: int | None
    weed_nettle: int | None
    weed_ragweed: int | None
    weed_risk: str | None
    weed: int | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Pollen:
        """Return Pollen object from the Ambee API response.

        Args:
            data: The data from the Ambee API.

        Returns:
            A Pollen object.
        """
        data = data["data"][0]
        count = data.get("Count", {})
        risk = data.get("Risk", {})
        species = data.get("Species", {})
        grass = species.get("Grass", {})
        tree = species.get("Tree", {})
        weed = species.get("Weed", {})

        return Pollen(
            grass_poaceae=grass.get("Grass / Poaceae"),
            grass_risk=risk.get("grass_pollen"),
            grass=count.get("grass_pollen"),
            tree_alder=tree.get("Alder"),
            tree_birch=tree.get("Birch"),
            tree_cypress=tree.get("Cypress"),
            tree_elm=tree.get("Elm"),
            tree_hazel=tree.get("Hazel"),
            tree_oak=tree.get("Oak"),
            tree_pine=tree.get("Pine"),
            tree_plane=tree.get("Plane"),
            tree_poplar=tree.get("Poplar / Cottonwood"),
            tree_risk=risk.get("tree_pollen"),
            tree=count.get("tree_pollen"),
            weed_chenopod=weed.get("Chenopod"),
            weed_mugwort=weed.get("Mugwort"),
            weed_nettle=weed.get("Nettle"),
            weed_ragweed=weed.get("Ragweed"),
            weed_risk=risk.get("weed_pollen"),
            weed=count.get("weed_pollen"),
        )


@dataclass
class Weather:
    """Object representing an Weather response from Ambee."""

    apparent_temperature: float | None
    cloud_cover: float | None
    dew_point: float | None
    humidity: float | None
    ozone: float | None
    pressure: float | None
    temperature: float | None
    time: int | None
    visibility: int | None
    wind_bearing: int | None
    wind_gust: float | None
    wind_speed: float | None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Weather:
        """Return Weather object from the Ambee API response.

        Args:
            data: The data from the Ambee API.

        Returns:
            A Weather object.
        """
        data = data["data"]
        return Weather(
            apparent_temperature=data.get("apparentTemperature"),
            cloud_cover=data.get("cloudCover"),
            dew_point=data.get("dewPoint"),
            humidity=data.get("humidity"),
            ozone=data.get("ozone"),
            pressure=data.get("pressure"),
            temperature=data.get("temperature"),
            time=data.get("time"),
            visibility=data.get("visibility"),
            wind_bearing=data.get("windBearing"),
            wind_gust=data.get("windGust"),
            wind_speed=data.get("windSpeed"),
        )
