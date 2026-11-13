###########################################################################
# C/H200 Introduction to Computers & Programming
# Indiana University, Bloomington, IN, USA
# Copyright MM Dalkilic
# Homework 9
# no part of this may be used or shared without express permission of author
###########################################################################

import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


###########################################################################
# Functions for Problem 1
###########################################################################
# leave this function
# helps with heatmap visualization
def make_IDs(people):
    return {tuple(p):ID for ID, p in enumerate(people)}

#INPUT a nested list of people encoded as 0's and 1's. v0 and v1 are the respective lists respresenting the people pairs.
#   You'll be comparing the smallest degree of difference between each sublist representing each person.
#RETURN person pair with the smallest degree (smallest degree of difference between the person pair lists)
def inner_prod(v0,v1):
    total = 0
    for a, b in zip(v0, v1):
        total += a * b
    return total

def mag(v):
    return math.sqrt(inner_prod(v, v))

def angle(v0,v1):
    cos_theta = inner_prod(v0, v1) / (mag(v0) * mag(v1))
    cos_theta = max(-1, min(1, cos_theta))  # guards against floating point drift
    radians = math.acos(cos_theta)
    return round(radians * 180 / math.pi, 2)

def match(people):
    result = []
    for i in range(len(people)):
        for j in range(i + 1, len(people)):
            result.append([people[i], people[j], angle(people[i], people[j])])
    return result

def best_match(scores):
    ranked = sorted(scores, key=lambda s: s[2])
    return tuple(ranked[0])
 
########################
# PROBLEM 2
########################

def msi(x):
   best_sum = x[0]
   best_start = 0
   best_stop = 1
   for start in range(len(x)):
        for stop in range(start + 1, len(x) + 1):
            s = sum(x[start:stop])
            if s > best_sum:
                best_sum = s
                best_start = start
                best_stop = stop
   return [best_start, best_stop, best_sum]
    
########################
# PROBLEM 3
########################

#INPUT list of 0s 1s
#OUTPUT longest list of 1s
def L(x):
    longest = 0
    current = 0
    for v in x:
        if v == 1:
            current += 1
            if current > longest:
                longest = current
        else:
            current = 0
    return longest

########################
# PROBLEM 4 Pirate Problem
########################
#input sides a,b and angle between
#output length opposite to angle
def cosine_law(a,b,angle):
    theta = math.radians(angle)  # math.cos expects radians
    return math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(theta))
#intput start time, stop time, speed
#output distance 
def distance(start,stop,speed):
    return (stop - start)*speed

########################
# PROBLEM 5
########################
# Optimization problems
# need to us NumPy
# Return ((price, revenue), attendance) for the revenue-maximizing
# ticket price, searching prices 0.00, 0.01, ..., 10.00.
import numpy as np
def best_ticket_price():
    slope = (60000 - 70000) / (7 - 6)
    intercept = 70000 - slope * 6

    prices = np.arange(0, 10.01, .01)
    attendance = slope * prices + intercept
    revenue = prices * attendance + 1.50 * attendance

    i = revenue.argmax()
    return ((float(prices[i]), float(revenue[i])), float(attendance[i]))

###########################################################################
# Functions for Problem 6
###########################################################################
#various business models
#price 
def p(x):
    return 5.00 - 0.002*x
#revenue
def R(x):
    return x*p(x)
#cost
def C(x):
    return 3.00 + 1.10*x
#profit
def P(x):
    return R(x) - C(x)

#input profit function and interval of units sold
#output tuple (maximal profit, unit)
def max_revenue(R,a,b):
    best_x = a
    best_val = R(a)
    for x in range(a, b + 1):
        if R(x) > best_val:
            best_val = R(x)
            best_x = x
    return (best_val, best_x)



if __name__ == "__main__":

    ''' use this space to call your functions

    '''
    # problem 1
    people0 = [[1,1,1,1,0],[0,0,1,1,1],[0,0,0,1,1]]
    print(match(people0))
    print(best_match(match(people0)))

    # people1 = [[0,1,1,0,0,0,1],
    #            [1,1,0,1,1,1,0],
    #            [1,0,1,1,0,1,1],
    #            [1,0,0,1,1,0,0],
    #            [0,0,0,1,1,0,0],
    #            [0,1,0,1,0,1,0],
    #            [1,1,1,0,0,1,0]]
    # matches = match(people1)
    # print(matches)
    # print(best_match(matches))

    #####################################################
    # uncomment below keeping line 150- uncomments too 
    # to see visualization
    ####################################################
    # people_IDs = make_IDs(people1)
    # print(people_IDs)
    # IDs = list(people_IDs.values())
    # df = pd.DataFrame(1.0, index=IDs, columns=IDs)
    # for p1, p2, score in matches:
    #     df.loc[people_IDs[tuple(p1)], people_IDs[tuple(p2)]] = round(1-score/90,2)
    #     df.loc[people_IDs[tuple(p2)], people_IDs[tuple(p1)]] = round(1-score/90,2)
            
    # sns.heatmap(df, annot=True, cmap='YlGnBu', vmin=0, vmax=1, linewidths=0.5)
    # plt.show()

    # p1,p2,score = best_match(match(people1))
    # print(f"{people_IDs[tuple(p1)],people_IDs[tuple(p2)]} {score}")
    # # print(best_match(match(people1)))
    # # #output is ([1, 0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 1, 0, 0], 35.26)

    v0,v1 = (2,3,-1), (1,-3,5)
    print(angle(v0,v1)) #122.83

    v0,v1 = (3,4,-1),(2,-1,1)
    print(angle(v0,v1)) #85.41

    v0,v1 = (5,-1,1),(1,1,-1)
    print(angle(v0,v1)) #70.53


    # Problem 2
    x2 = [7, -9, 5, 10, -9, 6, 9, 3, 3, 9]
    print(msi(x2))

 
    # Problem  3
    data3 = [[0],[1],[1,1,0,1,1,1],[0,1,1,0],[0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    for d in data3:
        print(L(d))

    # Problem 4
    Sa = 24   
    Sb = 18
    start_a = 1
    start_b = 1.5
    stop = 3
    a,b = 34,56
    print(cosine_law(*(distance(start_a,stop,Sa),distance(start_b,stop,Sb)),a+b))
    
    #problem  5
    print(best_ticket_price())

    
    #problem 6
    p_,u_ = max_revenue(P,1,1000)
    print(u_)    
    # visualization    
    x = np.linspace(1,1299,100)
    y = P(x)
    plt.plot(x,y,'r')
    plt.plot(u_,p_,'go')
    plt.xlabel("Units")
    plt.ylabel("Revenue $MM")
    plt.title ("Maximizing Revenue")
    plt.show()

    