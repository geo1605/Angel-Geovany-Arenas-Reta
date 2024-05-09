import math

d = 10000
a = 0.0
c_A = 0.0
acom = 0

for i in range(d):
    acom += 1
    baseT = acom/float(d)
    alt = math.sqrt(1-baseT*baseT)
    base = 1/float(d)
    c_A += base * alt
pi = c_A*4
