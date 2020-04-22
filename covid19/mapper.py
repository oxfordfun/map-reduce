# Covid19 mapper

class Mapper:
    def map_continent(self, data, continent):
        '''
        map and combine daily records for each country
        '''
        country_records = []
        ## Map all records according to countries [(country, record), [county, record]]
        for record in data:
            if record['continentExp'] == continent:
                country = record['countriesAndTerritories']
                cases = record['cases']
                deaths = record ['deaths']
                population = record['popData2018']
                country_records.append((country, record))

        country_combined = {}

        for country, record in country_records:
            if country not in country_combined.keys():
                country_combined[country] = [record]
            else:
                country_combined[country].append(record)

        return country_combined
        
