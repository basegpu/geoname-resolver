import argparse
import sys
from colorama import Fore, Style
from logging import Logger

logger = Logger(__name__)

class MyParser(argparse.ArgumentParser):

    def error(self, message):
        logger.error(Fore.RED + f'\n{message}\n' + Fore.RESET)
        self.print_help()
        sys.exit(2)

parser = MyParser(description=Style.BRIGHT + 'Lookup geographical places.' + Style.RESET_ALL)
parser.add_argument('--username', metavar='U', type=str, required=True, help='GeoNames username')
parser.add_argument('--places', metavar='P', type=str, nargs='+', help='places to be processed')
parser.add_argument('--file', metavar='f', type=str, help='file to read places from')
parser.add_argument('--output', metavar='o', type=str, help='file to write the output, otherwise it will be printed to the console (default)')

# everything we need from command line arguments is in the parser
args = parser.parse_args()

if args.file is None and args.places is None:
    parser.error('Either define places with --places, provide a file with --file, or both.')