import numpy as np
import random as rn
import math

# problem 1
#input array of report IDs (as +integers)
#output two lists: list1 = unique IDs, list2 = [(id,cnt),...] ids and occurrences
def duplicate_reports(r_ids):
    counts = {}
    for rid in r_ids.tolist():
        counts[rid] = counts.get(rid, 0) + 1

    unique = []
    duplicates = []
    for rid, cnt in counts.items():
        if cnt == 1:
            unique.append(rid)
        else:
            duplicates.append((rid,cnt))
    return unique, duplicates
# problem 2
# input two NumPy array
# output dot product
# cannot use NumPy.dot(x,y)
def my_scalar(x,y):
    total = 0
    for i in range(len(x)):
        total += x[i] * y[i]
    return total

# problem 3
# input NumPy array
# output magnitude
# must use my_scalar
# cnnot use NumPy.linalg.norm(x)
def my_magnitude(x):
    return math.sqrt(my_scalar(x, x))

# problem 4
# input two NumPy arrays
# output cos in degrees
# must use my_scalar, my_magnitude
# cannot use NumPy functions
# two decimal places
def my_cos(x,y):
    c = my_scalar(x, y) / (my_magnitude(x) * my_magnitude(y))
    c = max(-1, min(1, c))
    return round(math.degrees(math.acos(c)), 2)

# problem 5
#input proportion of house seats
#output proportion of presidential vote
# three decimal places
def required_presidential_vote(h):
    k = (h / (1 - h)) ** (1 / 3)
    return round(k / (1 + k), 3)

# problem 6
# input data described in HW
# output average of 1st,2nd 6-months
# this is done for you!
def q1(d):
    n = len(d)
    A = sum([x for _,(x,y) in d])/n
    B = sum([y for _,(x,y) in d])/n
    return round(A,2),round(B,2)

#input data
#output returns names of sales people who
#had zero sales either half
#must use comprhension
def q2(d):
    return [name for name, (x, y) in d if x == 0 or y == 0]

#input data
#output returns names of people who were better than the average
#of both halfs
def q3(d):
    n = len(d)
    A = sum([x for _,(x,y) in d])/n
    B = sum([y for _,(x,y) in d])/n
    return [name for name, (x, y) in d if x >= A and y >= B]

#input data
#output returns names of max sales (sum of both 6 months)
def q4(d):
    best = max([x + y for _, (x, y) in d])
    return [name for name, (x, y) in d if x + y == best]

# problem 7
#input coef = (a,b,c) for ax^2 + bx + c
#output tuple ( 'up'|'down',(vertex,y-value of vertex) )
# round to two decimal places
def q(coef):
    a, b, c = coef
    vx = -b / (2 * a)
    vy = a * vx ** 2 + b * vx + c
    direction = "down" if a < 0 else "up"
    return (direction, (round(vx, 2), round(vy, 2)))
#problem 8
#input time, speed1, speed2 both heading in same direction
#output time train 2 reaches train 1
# round 2 decimal places
def train_type1(t0,s1,s2):
    return round(t0 * s1 / (s2 - s1), 2)

#input speed 1, speed 2, distance heading towards each other
#output time to reach each other
# round 2 decimal places
def train_type2(s1,s2,d):
    return round(d / (s1 + s2), 2)

#problem 9
#input n >= k, use math module
#output nCr
def C(n,k):
    return math.factorial(n) / (math.factorial(n - k) * math.factorial(k))

############# do not change the following line ###################
if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the unit testing Feel free to add print statements. 
    You should uncomment *after* you've completed the function
    """

# uncomment to see output
# problem 1
report_ids = np.array([rn.randint(0,10) for _ in range(rn.randint(1,10))],dtype=int)
print(report_ids)
print(duplicate_reports(report_ids))

#problem 2
a2 = np.array([1,2,3])
b2 = np.array([-3,4,0])
print(my_scalar(a2,b2),np.dot(a2,b2))
r2_r = rn.randint(2,10)
x2,y2 = np.array([rn.randint(-10,10) for _ in range(r2_r)]),np.array([rn.randint(-10,10) for _ in range(r2_r)])
print(x2,y2)
print(my_scalar(x2,y2),np.dot(x2,y2))

#problem 3
a3 = np.array([1,2,3])
print(my_magnitude(a3), np.linalg.norm(a3))
r3_r = rn.randint(2,10)
x3 = np.array([rn.randint(-10,10) for _ in range(r3_r)])
print(my_magnitude(x3),np.linalg.norm(x3))

#problem 4
x4 = np.array([1,0,0,1])
y4 = np.array([0,1,0,1])
a = np.dot(x4,y4)/(np.linalg.norm(x4)*np.linalg.norm(y4))
print(math.degrees(math.acos(a)),my_cos(x4,y4))

x4_1 = np.array([3,4])
y4_1 = np.array([8,15])
a = np.dot(x4_1,y4_1)/(np.linalg.norm(x4_1)*np.linalg.norm(y4_1))
print(my_cos(x4_1,y4_1),math.degrees(math.acos(a)))

# problem 5
p5 = lambda x:(x**3)/(x**3 + (1-x)**3)
house_seats = 60/100
pres_vote = .534
print(p5(pres_vote), required_presidential_vote(house_seats), p5(required_presidential_vote(house_seats)))

# problem 6
d6 = [('a',(4,4)),('b',(0,5)),('c',(4,5)),('d',(3,2))]
print(q1(d6))
print(q2(d6))
print(q3(d6))
print(q4(d6))

# problem 7
d7 = [(-2.6,7.6,-10),(1,-10.2,26.01)]
verticies = [q(d) for d in d7]
print(verticies)

# #problem 8
t0_12,s1_12,s2_12 = 2,40,60
print(f"Time = {train_type1(t0_12,s1_12,s2_12)} hr")
d_12 = 400
print(f"Time = {train_type2(s1_12,s2_12,d_12)} hr")

#problem 9
print(C(8,3))
