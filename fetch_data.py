# -*- coding: utf-8 -*-
"""
@author: Timothy Johnstone
"""

import os
import re
import sys
import argparse
import yelp
import json
import pickle
from time import sleep
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from collections import namedtuple

def parse_cmd(args):
    """ Parses user-supplied command line arguments """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-i', '--identity', type=str, required=True)
    parser.add_argument('-r', '--restaurant-list', type=str, required=True)
    parser.add_argument('-o', '--outfile', type=str, required=True)
    parser.add_argument('-c', '--city', type=str, required=True)
#    parser.add_argument('-n', '--nmer_size', type=int, default=7)  # configurable nmer size for searching
    optS = parser.parse_args(args)
    return optS

def authenticate_client(authfile_path):
    ''' Grabs api auth info from a simple json containing api keys '''
    with open(authfile_path) as authfile:
        creds = json.load(authfile)
        auth = Oauth1Authenticator(**creds)
        client = Client(auth)
    return client
    
def get_top_result(client, city, restaurant):
    ''' Searches a city for a given restaurant and returns the top result '''
    params = {
        'term': restaurant,
        'lang': 'en',
        'limit': 1,
        'category_filter': 'restaurants'
    }
    results = client.search(city, **params)
    # TODO handle bad queries / no results?
    return results

def wait(secs):
    print('Sleeping for {} seconds'.format(str(secs)), file=sys.stderr)
    sleep(secs)

def main(argv=None): 
    args = parse_cmd(argv[1:])
    # Initialize client
    client = authenticate_client(args.identity)
    # Grab the top result for each query from the API search endpoint
    result_list = []
    with open(args.restaurant_list) as rl:
        for restaurant in rl:
            if not restaurant.strip() == '':
                result_list.append(get_top_result(client, args.city, restaurant))
                wait(1)
    # Write out to file, pickled for now
    # TODO maybe more readable? eg yaml/json
    with open(args.outfile, 'wb') as outfile:
        pickle.dump(result_list, args.outfile)

if __name__ == '__main__':
    main(sys.argv)













