import argparse
import sys

from OutputWriter import OutputWriter


class MyParser(argparse.ArgumentParser):

    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

parser = MyParser(description='Lookup geographical places.')
parser.add_argument('--username', metavar='U', type=str, required=True, help='GeoNames username')
parser.add_argument('--places', metavar='P', type=str, required=True, nargs='+', help='places to be processed')
parser.add_argument('--output', metavar='o', type=OutputWriter.TYPES, default=OutputWriter.TYPES.CONSOLE, help='where to write the output (console, file)')