from typing import Any
from geopy.geocoders import GeoNames
from geopy.location import Location

class LocationFetcher:

    _geo: GeoNames
    _nrows: int

    def __init__(self, username: str, nrows: int = 1):
        # initialize with your username
        self._geo = GeoNames(username=username)
        self._nrows = nrows

    def get(self, name: str) -> list[Location]:
        # get location information
        try:
            candidates = self._geo.geocode(name, exactly_one=False)
            if not candidates:
                return []
            elif len(candidates) <= self._nrows:
                return candidates
            else:
                return candidates[:self._nrows]
        except Exception:
            raise Exception('Error fetching location information.')