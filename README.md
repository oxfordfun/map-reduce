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
4. Example of output [data/world.json](data/world.json)
```json
{
    "Top_Deaths": {
        "United_States_of_America": 42539,
        "Italy": 24114,
        "Spain": 20852,
        "France": 20265,
        "United_Kingdom": 16509,
        "Belgium": 5828,
        "Iran": 5209,
        "China": 4636,
        "Germany": 4598,
        "Netherlands": 3751
    },
    "Top_Cases": {
        "United_States_of_America": 787752,
        "Spain": 200210,
        "Italy": 181228,
        "Germany": 143457,
        "United_Kingdom": 124743,
        "France": 114657,
        "Turkey": 90980,
        "China": 83849,
        "Iran": 83505,
        "Russia": 47121
    },
    "Top_Infection": {
        "Cases_on_an_international_conveyance_Japan": 23.2,
        "San_Marino": 1.37,
        "Andorra": 0.93,
        "Holy_See": 0.9,
        "Luxembourg": 0.59,
        "Iceland": 0.5,
        "Spain": 0.43,
        "Gibraltar": 0.39,
        "Faroe_Islands": 0.38,
        "Guernsey": 0.38
    },
    "Top_Mortality": {
        "British_Virgin_Islands": 20.0,
        "France": 17.67,
        "Burundi": 16.67,
        "Nicaragua": 15.38,
        "Sint_Maarten": 14.71,
        "Belgium": 14.58,
        "Mauritania": 14.29,
        "Northern_Mariana_Islands": 14.29,
        "Algeria": 14.13,
        "Bahamas": 14.06
    }
}
```
### Dataset
Covid19 - [ECDC](https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide)

### Reference
Lämmel, R. (2008). "Google's Map Reduce programming model — Revisited". Science of Computer Programming. 70: 1–30. 

D. Miner, A. Shook, MapReduce Design Patterns: Building Effective Algorithms and Analytics for Hadoop and Other Systems, ” O’Reilly Media, Inc.”, USA, 2012.

R. Johansson, Numerical Python. Apress, 01 2019.
