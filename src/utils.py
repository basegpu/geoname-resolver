from pathlib import Path
from logging import Logger

logger = Logger(__name__)


def combine_list_and_file(list_arg: list[str] = [], file_arg: Path = None) -> list[str]:
    if file_arg:
        try:
            with open(file_arg, 'r') as f:
                places = f.read().splitlines()
        except FileNotFoundError:
            logger.error(f'File {file_arg} not found.')
            places = []
    return places + list_arg