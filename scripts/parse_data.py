# -*- coding: utf-8 -*-
"""
@author: Timothy Johnstone
"""

import sys
import argparse
import yelp
import pickle

def parse_cmd(args):
    """ Parses user-supplied command line arguments """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-i', '--infile', type=str, required=True)
    parser.add_argument('-j', '--json_outfile', type=str, required=True)
    parser.add_argument('-l', '--locations_outfile', type=str, required=True)
    optS = parser.parse_args(args)
    return optS

def extract_results(res):
    # TODO check if result is empty
    if len(res.businesses) > 0:
        res = res.businesses[0]
        d = {}
        d['Name'] = res.name #TODO image too?
        d['Category'] = res.categories[0].name
        d['Neighborhood'] = res.location.neighborhoods[0]
        d['Rating'] = res.rating #TODO make numeric sortable AND image. Num reviews? link to yelp?
        d['Phone'] = res.display_phone # TODO link to phone:res.phone
    else:
        print('No results found for query') # TODO check when fetching instead?

def main(argv=None): 
    args = parse_cmd(argv[1:])
    # Load in data
    with open(args.infile, 'rb') as infile:
        restaurants = pickle.load(infile)
    table_list = []
    for r in restaurants:
        table_list.append(extract_results(r))

if __name__ == '__main__':
    main(sys.argv)













