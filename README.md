## MapReduce Design Patterns with Covid19 data
We use MapReduce design patterns to analyze Covid19 data. 

### Get Started
1. Get code
```bash
   git clone https://github.com/oxfordfun/map-reduce
```
2. Get data
```bash
   cd map_reduce
   wget https://opendata.ecdc.europa.eu/covid19/casedistribution/json/ -O data/covid19.json
```
3. Run script
```bash
   python3 covid19/main.py data/covid19.json > data/output.json
```
4. Example of output [data/output.json](data/output.json)
```json
   {
    "United_States_of_America": {
        "deaths": 42539,
        "cases": 787752,
        "mortality_rate": 5.4,
        "infection_rate": 0.24,
        "2018population": "327,167,434",
        "dateRep": "21/04/2020"
    },
    "Italy": {
        "deaths": 24114,
        "cases": 181228,
        "mortality_rate": 13.31,
        "infection_rate": 0.3,
        "2018population": "60,431,283",
        "dateRep": "21/04/2020"
    },
    "Spain": {
        "deaths": 20852,
        "cases": 200210,
        "mortality_rate": 10.42,
        "infection_rate": 0.43,
        "2018population": "46,723,749",
        "dateRep": "21/04/2020"
    },
    "France": {
        "deaths": 20265,
        "cases": 114657,
        "mortality_rate": 17.67,
        "infection_rate": 0.17,
        "2018population": "66,987,244",
        "dateRep": "21/04/2020"
    },
    "United_Kingdom": {
        "deaths": 16509,
        "cases": 124743,
        "mortality_rate": 13.23,
        "infection_rate": 0.19,
        "2018population": "66,488,991",
        "dateRep": "21/04/2020"
    }
   }
```

### Dataset
Covid19 - [ECDC](https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide)

### Reference
Lämmel, R. (2008). "Google's Map Reduce programming model — Revisited". Science of Computer Programming. 70: 1–30. 

D. Miner, A. Shook, MapReduce Design Patterns: Building Effective Algorithms and Analytics for Hadoop and Other Systems, ” O’Reilly Media, Inc.”, USA, 2012.

R. Johansson, Numerical Python. Apress, 01 2019.
