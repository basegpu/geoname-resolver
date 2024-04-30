from pathlib import Path
from typing import Any, Callable

from colorama import Fore


class OutputWriter():
    
    _write: Callable[[str, Any | None], None]
    _file: Path | None

    def __init__(self, file: Path) -> None:
        if file:
            self._write = self._write_to_file
            self._file = file
        else:
            self._write = self._write_to_console
    
    def _write_to_console(self, key: str, location: Any | None) -> None:
        # print the results to the console
        if location:
            print(Fore.GREEN + f'{key}: {location}' + Fore.RESET)
        else:
            print(Fore.RED + f'{key}: NOT FOUND.' + Fore.RESET)
    
    def _write_to_file(self, key: str, location: Any | None) -> None:
        # write the results to a file
        with open(self._file, 'a') as f:
            if location:
                f.write(f'{key}: {location}\n')
            else:
                f.write(f'{key}: NOT FOUND.\n')
    
    def process(self, key: str, location: Any | None) -> None:
        self._write(key, location)