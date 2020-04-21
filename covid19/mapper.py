# Covid19 mapper

class Mapper:
    def keyword_sum(self, data, keyword):
        '''
        map (country, keyword) to (country, sum(keyword))
        '''
        counts = []
        for record in data:
            country = record['countriesAndTerritories']
            item = record[keyword]
            counts.append((country, item))
        
        mapped = {}
        for k, v in counts:
            if k not in mapped:
                mapped[k] = int(v)
            else:
                mapped[k] = mapped[k] + int(v)
        return mapped

    def keyword_filter(self, data, keyword, value):
        '''
        filter record only while keyword = value
        '''
        counts = []
        for record in data:
            if record[keyword] == value:
                counts.append(record)
        return counts
