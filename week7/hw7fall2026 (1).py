import math
import random as rn
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

###########################################################################
# Functions for Problem 1
###########################################################################
#INPUT dlst = array [x,y] x,y >= 3 of zeros 
#RETURN outer edges decorated with 0,1,2,3,... clockwise
def decorate(arr):
    out = arr.copy()
    rows, cols = out.shape
    n = 0

    for c in range(cols):
        out[0, c] = n
        n += 1

    for r in range(1, rows):
        out[r, cols - 1] = n
        n += 1

    for c in range(cols - 2, -1, -1):
        out[rows - 1, c] = n
        n += 1

    for r in range(rows - 2, 0, -1):
        out[r, 0] = n
        n += 1
    return out

for i in range(3, 7):
    for j in range(3, 7):
        mario_kart = np.zeros((i, j), dtype=int)
        print(mario_kart)
        print(decorate(mario_kart))


###########################################################################
# Functions for Problem 2
###########################################################################
#INPUT t = (a,b,c)
#RETURN return complex or real roots
def q(t):
    a, b, c = t
    disc = b**2 - 4*a*c
 
    if disc >= 0:
        s = math.sqrt(disc)
        r0 = (-b - s) / (2*a)
        r1 = (-b + s) / (2*a)
        lo, hi = min(r0, r1), max(r0, r1)
        return (round(lo, 2) + 0.0, round(hi, 2) + 0.0)
    else:
        re = -b / (2 * a)
        im = math.sqrt(-disc) / (2*a)
        re = round(re, 2) + 0.0
        im = round(abs(im), 2)
        return (complex(re, im), complex(re, -im))


###########################################################################
# Functions for Problem 3
###########################################################################
# input polynomial coefficient, linear coeff
# polynomial divsion coefficient 

def sd(p,q):
    b1, b0 = q
    x = -b0 / b1
    y = p[0]
    ans = [y]
 
    for i in range(1, len(p)):
        y = x * y + p[i]
        ans.append(y)
 
    if b1 != 1:
        ans = [c * (1 / b1) for c in ans[:-1]] + [ans[-1]]
    return ans

###########################################################################
# Functions for Problem 4
###########################################################################
#INPUT galaxy data: name, velocity, distance
#output approx age of universe in billion years 
#CONSTRAINT round 2 places
def approx_age(data):

    # we're giving this to you
    x = np.array([x for _,_,x in data]).reshape(-1,1)
    y = np.array([y for _,y,_ in data])

 
    model = LinearRegression(fit_intercept=False)
    model.fit(x, y)
    H0 = model.coef_[0]
 
    km_per_mpc = 3.09e13 * 1e6
    seconds = km_per_mpc / H0
 
    years = seconds / (60 * 60 * 24 * 365.25)
    return round(years / 1e9, 2)

###########################################################################
# Functions for Problem 5
###########################################################################
#INPUT values for annuity
#OUTPUT deposit amount needed
def deposit(S,i,n):
    return S * i / ((1 + i)**n - 1)
#INPUT sinking fund values except deposit
#OUTPUT a list of period, deposit, interest, accrued total fund
def sinking_fund(final_amt, r, m, y):
     i = r / m
     n = m * y
     R = round(deposit(final_amt, i, n), 2)

     total = R
     schedule = [[0, R, 0, total]]
 
     for period in range(1, n):
        interest = round(i * total, 2)
        total = round(total + interest + R, 2)
        schedule.append([period, R, interest, total])

     return schedule


if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You **do not** have to put anything here
    """

    # problem 1
    # for i in range(3,7):
    #     for j in range(3,7):
    #         mario_kart = np.zeros((i,j),dtype=int)
    #         print(mario_kart)
    #         print(decorate(mario_kart))

    #problem 2
    # print(q((3,4,2)))
    # print(q((1,3,-4)))
    # print(q((1,-2,-4)))

    #  problem 3
    # data_3 = [((2,-5,3,7),((1/2),-1)),((3,0,5,-1),(1,1)),((4,-8,-1,5),(2,-1))]
    # for d in data_3:
    #     print(sd(*d))


    # problem 4 galaxy name, velocity, distance
    # galaxy_data = [['NGC0925', 664, 9.16], ['NGC1326A', 1794, 16.14], ['NGC1365', 1594, 17.95], 
    #            ['NGC1425', 1473, 21.88], ['NGC2403', 278, 3.22], ['NGC2541', 714, 11.22], 
    #            ['NGC2090', 882, 11.75], ['NGC3031', 80, 3.63], ['NGC3198', 772, 13.8], 
    #            ['NGC3351', 642, 10.0], ['NGC3368', 768, 10.52], ['NGC3621', 609, 6.64], 
    #            ['NGC4321', 1433, 15.21], ['NGC4414', 619, 17.7], ['NGC4496A', 1424, 14.86], 
    #            ['NGC4548', 1384, 16.22], ['NGC4535', 1444, 15.78], ['NGC4536', 1423, 14.93], 
    #            ['NGC4639', 1403, 21.98], ['NGC4725', 1103, 12.36], ['IC4182', 318, 4.49], 
    #            ['NGC5253', 232, 3.15], ['NGC7331', 999, 14.72]]
    # print(approx_age(galaxy_data))

    # problem 5
    # S9 = 30000
    # m9 = 4
    # r9 = 10/100
    # y9 = 2
    # for i in sinking_fund(S9,r9,m9,y9):
    #     print(i)

