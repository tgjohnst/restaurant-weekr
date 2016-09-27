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
    d = {}
    d['Name'] = res.name #TODO image too?
    d['Category'] = res.categories[0].name
    d['Neighborhood'] = res.location.neighborhoods[0]
    d['Rating'] = res.rating #TODO make numeric sortable AND image. Num reviews? link to yelp?
    d['Phone'] = res.display_phone # TODO link to phone:res.phone

def extract_location(res):
    rname = r.name
    rloc = r.loc
    # TODO
    return ________

def main(argv=None): 
    args = parse_cmd(argv[1:])
    # Load in data
    with open(args.infile, 'rb') as infile:
        restaurants = pickle.load(infile)
    table_list = []
    loc_list = []
    for r in restaurants:
        if len(r.businesses) > 0:
            r = r.businesses[0]        
            table_list.append(extract_results(r))
            loc_list.append(extract_location(r))

if __name__ == '__main__':
    main(sys.argv)













