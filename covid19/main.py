#! /usr/bin/env python3
# download covid19 data: wget https://opendata.ecdc.europa.eu/covid19/casedistribution/json/ -O data/covid19.json
# python3 covid19/main.py data/covid19.json > data/output.json

import sys
import json

from mapper import Mapper
from reducer import Reducer


if __name__ == "__main__":
    input_file = sys.argv[1]
    with open(input_file) as reader:
        all_data = json.loads(reader.read())
        data = all_data['records']
    
    # mapped to country

    mapper = Mapper()
    country_data = mapper.map_continent(data,'Europe')
    
    # get stats of each country
    reducer = Reducer()
    country_stats = reducer.get_country_stats(country_data)
    country_deaths_counts, country_cases_counts, country_mortality_counts, country_infection_counts = reducer.slice_country_stats(country_stats)

    # sort the data
    final_result = {}
    sorted_deaths = reducer.sort(country_deaths_counts, 10)
    final_result['Top_Deaths'] = sorted_deaths
    sorted_cases = reducer.sort(country_cases_counts,10)
    final_result['Top_Cases'] = sorted_cases
    sorted_infection = reducer.sort(country_infection_counts,10)
    final_result['Top_Infection'] = sorted_infection
    sorted_mortality = reducer.sort(country_mortality_counts,10)
    final_result['Top_Mortality'] = sorted_mortality

    output_json = json.dumps(final_result, indent=4)
    print(output_json)