# Covid19 reducer

class Reducer:
    def sort(self, data):
        '''
        sort data (a dictionary) based on values descending
        '''
        
        sorted_data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}

        return list(sorted_data.items())

    def country_reduce(self,data):
        '''
        group summary of country data on death, cases, mortality rate, infection rate
        '''

        import datetime
        counts = {}
        counts['deaths'] = 0
        counts['cases'] = 0
        day = datetime.datetime.strptime('01/01/2020', '%d/%m/%Y').date()
        population = int(data[0]['popData2018'])
        for record in data:
            deaths = int(record['deaths'])
            cases = int(record['cases'])
            date_record = datetime.datetime.strptime(record['dateRep'], "%d/%m/%Y").date()
            if date_record > day:
                day = date_record 
            counts['deaths'] = counts['deaths'] + deaths
            counts['cases'] = counts['cases'] + cases
        counts['mortality_rate'] = round(counts['deaths'] / counts['cases'] * 100 ,2)
        counts['infection_rate'] = round(counts['cases'] / population * 100 ,2)
        counts['2018population'] = '{:,}'.format(population)
        counts['dateRep'] = day.strftime("%d/%m/%Y")
        return counts

