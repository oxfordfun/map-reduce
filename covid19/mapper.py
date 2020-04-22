# Covid19 mapper

class Mapper:
    def map_continent(self, data, continent):
        '''
        input: 
        continent  - name of continent

        data - [{country-daily-record}*], e.g.
        { 
            "dateRep": "12/04/2020",
            "day": "12",
            "month": "4",
            "year": "2020",
            "cases": "8719",
            "deaths": "917",
            "countriesAndTerritories": "United_Kingdom",
            "geoId": "UK",
            "countryterritoryCode": "GBR",
            "popData2018": "66488991",
            "continentExp": "Europe"
        }
        
        output:
        country_combined - [{'{country}': [{country-daily-record}}*]]
        '''

        ## fliter records for the continent [(country_daily _ecord), [county_daily_ecord]]
        country_records = []
        
        for record in data:
            country = record['countriesAndTerritories']
            if continent in ['Europe', 'Asia', 'America', 'Africa', 'Oceania']:
                if record['continentExp'] == continent:
                    country_records.append((country, record))
            else:
                country_records.append((country, record))

        
        ## combine records for each country
        country_combined = {}

        for country, record in country_records:
            if country not in country_combined.keys():
                country_combined[country] = [record]
            else:
                country_combined[country].append(record)

        return country_combined
        
