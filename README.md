# Astronomical Event list generator
To generate a list of astronomical events within a time range and save it into an excel file. This excel file can be used as the Astro e-calander of the Hong Kong Space Museum in its Star Hopper moblie app and 

## How to run
test
```python
ts = api.load.timescale()
eph = api.load('de440.bsp')
HKT = timezone('Asia/Hong_Kong')
t0 = ts.utc(2021, 1, 1) - 1/3
t1 = ts.utc(2021, 12, 31) - 1/3
```
