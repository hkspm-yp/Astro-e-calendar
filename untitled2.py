from skyfield.api import load
from main import *
from skyfield.api import Star, load
# planets = load('de440.bsp')
# earth = planets['earth']

Spica = Star(ra_hours=(13, 26, 17), dec_degrees=(-11, 9, 40.5))
Regulus  = Star(ra_hours=(10, 8, 22.46), dec_degrees=(11, 58, 1.9))

# ts = load.timescale()
t = ts.utc(2020, 1, 1)

e = earth.at(t)
m = e.observe(moon)
s = e.observe(Spica)

ra, dec, distance = m.radec()
ra_s, dec_s, distance_s = s.radec()

print('RA:', ra)
print('Dec:', dec)
print('Distance:', distance)
