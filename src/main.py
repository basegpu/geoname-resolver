from ArgParser import parser
from LocationFetcher import LocationFetcher
from OutputWriter import OutputWriter


# everything we need from command line arguments is in the parser
args = parser.parse_args()

# create a fetcher object (using geoNames API)
fetcher = LocationFetcher(args.username)

# for each place in the list, get the location information
locations = { place: fetcher.get(place) for place in args.places }

# write results
OutputWriter.process(locations, args.output)