from enum import Enum
from typing import Any

from colorama import Fore


class OutputWriter():

    class TYPES(Enum):
        CONSOLE = 'console'
        FILE = 'file'
    
    @classmethod
    def process(cls, locations: dict[str, Any | None], type: TYPES) -> None:
        if type == cls.TYPES.CONSOLE:
            cls._write_to_console(locations)
    
    @staticmethod
    def _write_to_console(locations: dict[str, Any | None]) -> None:
        # write the results to the console
        for place, p in locations.items():
            if p:
                print(Fore.GREEN + f'{place}: {p}')
            else:
                print(Fore.RED + f'{place}: NOT FOUND.')