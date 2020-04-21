## MapReduce Design Patterns with Covid19 data
We use MapReduce design patterns to analyze Covid19 data. 

### Get Started
1. Get code
```bash
   git clone https://github.com/oxfordfun/map_reduce
```
2. Get data
```bash
   cd map_reduce
   wget https://opendata.ecdc.europa.eu/covid19/casedistribution/json/ -O data/covid19.json
```
3. Run script
```bash
   python3 covid19/main.py data/covid19.json
```

### Dataset
Covid19 - [ECDC](https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide)

### Reference
Lämmel, R. (2008). "Google's Map Reduce programming model — Revisited". Science of Computer Programming. 70: 1–30. 

D. Miner, A. Shook, MapReduce Design Patterns: Building Effective Algorithms and Analytics for Hadoop and Other Systems, ” O’Reilly Media, Inc.”, USA, 2012.

R. Johansson, Numerical Python. Apress, 01 2019.
