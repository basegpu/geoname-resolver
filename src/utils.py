from pathlib import Path
from logging import Logger

logger = Logger(__name__)


def combine_list_and_file(list_arg: list[str] | None, file_arg: Path | None) -> list[str]:
    places = [] if list_arg is None else list_arg
    if file_arg:
        try:
            with open(file_arg, 'r') as f:
                places = places + f.read().splitlines()
        except FileNotFoundError:
            logger.error(f'File {file_arg} not found.')
    return places