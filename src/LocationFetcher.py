from typing import Any
from geopy.geocoders import GeoNames


class LocationFetcher:

    _geo: GeoNames

    def __init__(self, username: str):
        # initialize with your username
        self._geo = GeoNames(username=username)

    def get(self, name: str) -> Any | None:
        # get location information
        try:
            return self._geo.geocode(name)
        except Exception:
            raise Exception('Error fetching location information.')