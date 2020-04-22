# Covid19 reducer

class Reducer:
    def count_country(self,records):
        '''
        Count data for one country
        '''
        import datetime
        counts = {}
        counts['deaths'] = 0
        counts['cases'] = 0
        day = datetime.datetime.strptime('01/01/2020', '%d/%m/%Y').date()
        for record in records:            
            deaths = int(record['deaths'])
            cases = int(record['cases'])
            if len(record['popData2018']) > 0:
                population = int(record['popData2018'])
            else:
                population = 1000000000
            date_record = datetime.datetime.strptime(record['dateRep'], "%d/%m/%Y").date()
            if date_record > day:
                day = date_record 
            counts['deaths'] = counts['deaths'] + deaths
            counts['cases'] = counts['cases'] + cases
        counts['mortality'] = round(counts['deaths'] / counts['cases'] * 100 ,2)
        counts['infection'] = round(counts['cases'] / population * 100 ,2)
        counts['population'] = population #'{:,}'.format(population)
        counts['dateRep'] = day.strftime("%d/%m/%Y")
        return counts
      
    def sort(self, data,n):
        '''
        sort data (a dictionary) based on values descending
        '''
        sorted_data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}
        list_sorted_data = list(sorted_data.items())[:n]

        return dict(list_sorted_data)

    def get_country_stats(self, country_record):
        '''
        Get country stats with all daily records of each country
        '''
        country_stats = {}
        for country, records in country_record.items():
            country_stats[country] = self.count_country(records)
        return country_stats
    
    def slice_country_stats(self, country_stats):
        country_deaths_counts = {}
        country_cases_counts = {}
        country_mortality_counts = {}
        country_infection_counts = {}
        country_population_counts = {}

        for country, stats in country_stats.items():
            deaths = int(stats['deaths'])
            country_deaths_counts[country] = deaths
            cases = int(stats['cases'])
            country_cases_counts[country] = cases
            mortality = float(stats['mortality'])
            country_mortality_counts[country] = mortality
            infection = float(stats['infection'])
            country_infection_counts[country] = infection
            population = int(stats['population'])
            country_population_counts[country] = population

        return country_deaths_counts, country_cases_counts, country_mortality_counts, country_infection_counts