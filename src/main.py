from MyParser import args
from LocationFetcher import LocationFetcher
from OutputWriter import OutputWriter
from utils import combine_list_and_file

# get all places to be processed
places = combine_list_and_file(args.places, args.file)

# create an output writer object
writer = OutputWriter(args.output)

# create a fetcher object (using geoNames API)
fetcher = LocationFetcher(args.username)

# for each place in the list, get the location information and write it
for place in places:
    location = fetcher.get(place)
    writer.process(place, location)