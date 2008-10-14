from math import *
from pylab import *
def am(t,fc,fm,a):
    t = float(t)
    fc = float(fc)
    fm = float(fm)
    a = float(a)

    return cos(2*pi*fc) + (a/2)*cos(2*pi*(fc+fm)*t) + (a/2)*cos(2*pi*(fc-fm)*t)

fc = 1200 
fm = 100
a = 2
x = []
y = []

for i in range(200):
    x.append(i)
    y.append(am(i,fc,fm,a))

plot(x,y)
show()
