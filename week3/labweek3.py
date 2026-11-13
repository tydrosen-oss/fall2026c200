# C200 Fall 2026, Lab 3
# Submit this file to Lab3 on Canvas (Assignments > Lab3) before the end of your lab.

import numpy as np
import math

# data
D = {(0,2),(1,4),(2,6)}

# separate x,y for numpy
x = np.array([x for x,_ in D])
y = np.array([y for _,y in D])


coeffs = np.polyfit(x, y, 2)

# returns list with coeffs a_2*(x**2) a_1(x**1) a_0(x**0)
print("coefficients: ", coeffs)

for x in range(5):
    print(x, np.polyval(coeffs,x))



#input years 1977 <= years <= 1997
#output function cost, -1 otherwise
def f(t):
    if 1977 <= t <= 1984:
        return (2/7)*(t-1977)+12
    elif 1984 < t <= 1987:
        return (t-1977)+7
    elif 1987 <t <= 1997:
        return (3/5)*(t-1977)+11
    else:
        return -1

data = [1976,1977,1985,1988,2000]

for d in data:
     print(d,f(d))


