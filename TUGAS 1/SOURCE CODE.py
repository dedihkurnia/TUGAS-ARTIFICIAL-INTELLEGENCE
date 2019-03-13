import math
from random import *

def f(x,y):
    return -abs(math.sin(x)*math.cos(y)*math.exp(abs(1-math.sqrt(x**2+y**2)/math.pi)))

SUHU = 100
UBAH = 0.9999
DATA = 100000
x = uniform(-10, 10)
y = uniform(-10, 10)

for i in range(1, DATA):
    x2 = uniform(-10, 10)
    y2 = uniform(-10, 10)
    SELISIH = f(x2, y2) - f(x, y)
    if SELISIH < 0:
        x = x2
        y = y2
    elif math.exp(-SELISIH/SUHU) > random():
        x = x2
        y = y2
    SUHU = SUHU*UBAH
print(f(x,y))
