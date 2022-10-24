# Astronomical Event list generator
To generate a list of astronomical events within a specified time range (e.g.: 1/1/2023 - 31/12/2023) and save it into an excel file. This excel file is made according to the Astro e-calander of the Hong Kong Space Museum.

## How to run

Python programming language has to be installed first. For simplify, user may install the Anaconda Distribution which includes the latest python versions and many useful python packages including jupyter, Numpy, pandas and Spyder, etc. To install Anaconda, please go to
https://www.anaconda.com


```python
ts = api.load.timescale()
eph = api.load('de440.bsp')
HKT = timezone('Asia/Hong_Kong')
t0 = ts.utc(2021, 1, 1) - 1/3
t1 = ts.utc(2021, 12, 31) - 1/3
```
