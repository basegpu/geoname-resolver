from pathlib import Path
from typing import Any, Callable
from geopy.location import Location

from colorama import Fore


class OutputWriter():
    
    _write: Callable[[str, Any | None], None]
    _file: Path | None

    def __init__(self, file: Path) -> None:
        if file:
            file.open('w').close()
            self._file = file
            self._write = self._write_to_file
        else:
            self._write = self._write_to_console
    
    def _write_to_console(self, key: str, locations: list[Location]) -> None:
        # print the results to the console
        if locations:
            for location in locations:
                print(Fore.GREEN + f'{key:<24}: {location} ({location.raw["geonameId"]})' + Fore.RESET)
        else:
            print(Fore.RED + f'{key:<24}: NOT FOUND' + Fore.RESET)
    
    def _write_to_file(self, key: str, locations: list[Location]) -> None:
        # write the results to a file
        with open(self._file, 'a') as f:
            if locations:
                for location in locations:
                    f.write(f'{key}; {location} ({location.raw["geonameId"]})\n')
            else:
                f.write(f'{key}; NOT FOUND\n')
    
    def process(self, key: str, locations: list[Location]) -> None:
        self._write(key, locations)