#! /usr/bin/env python3
# download covid19 data: wget https://opendata.ecdc.europa.eu/covid19/casedistribution/json/ -O data/covid19.json
# python3 covid19/main.py data/covid19.json > data/output.json

import sys
import json

from mapper import Mapper
from reducer import Reducer

def top_sum(data, keyword, top=10):
    '''
    Top sum for keyword 
    '''
    mapper = Mapper()
    mapped = mapper.keyword_sum(data, keyword)

    #print(f'mapped: {mapped}')

    reducer = Reducer()
    reduced = reducer.sort(mapped)

    #print(f'reduced {reduced}')

    if len(reduced) < top:
        return reduced
    else:
        return reduced[:top]

def query_country(data, keyword, value):

    '''
    One country data 
    '''
    mapper = Mapper()
    mapped = mapper.keyword_filter(data, keyword, value)

    #print(f'mapped: {mapped}')

    reducer = Reducer()
    reduced = reducer.country_reduce(mapped)

    #print(f'reduced {reduced}')
    return reduced


if __name__ == "__main__":
    input_file = sys.argv[1]
    with open(input_file) as reader:
        all_data = json.loads(reader.read())
        data = all_data['records']
    top_20 = top_sum(data, 'deaths',20)

    output = {}
    for country, death in top_20:
        stats = query_country(data, 'countriesAndTerritories', country)
        output[country] = stats
    
    output_json = json.dumps(output, indent=4)
    print(output_json)