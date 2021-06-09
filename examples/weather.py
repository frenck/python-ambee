# pylint: disable=W0621
"""Asynchronous Python client for the Ambee API."""

import asyncio

from ambee import Ambee


async def main():
    """Show example on getting Ambee data."""
    async with Ambee(api_key="example", latitude=12, longitude=77) as client:
        weather = await client.weather()
        print(weather)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
