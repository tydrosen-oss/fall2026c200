# Fall CH200 Fall 2026 IUB
# Dr. Dalkilic
# Laboratory & Homework 2

import math

# PROBLEM 1
# This is done in Lab
#####################
# input t days
# output oxygen content
def oxygen_content(t):
    n = t**2 + 5*t + 2
    d = t**2 + 3*t + 1

    result = 15 * (n / d)
    return result

# comment to stop output
# uncomment to see output
for t in range(5):
    print("days: ", t, "oxygen content ", oxygen_content(t))

print(oxygen_content(3.56155))

# Problem 2
# This is done for homework
#####################
#input b age with decimal, adult dosage in mg
#output adolescent dosage
def D(b,A):
    ceil_b = math.ceil(b)
    original = A * (ceil_b / 24)
    result = math.floor(original)
    return result

data = [(4.5,400),(5,400),(5.54,500)]
for b,A in data:
        print(b,A, D(b,A))

# uncomment to see output
# for b,A in data:
#     print(b,A, D(b,A))

# Problem 3
# This is done for homework
#######################
#input t time seconds
#output height feet
def height(t):
    result = -16*t**2 + 64*t + 80
    return result

# uncomment to see output
for t in range(6):
    print(t,height(t))

''' Triple quotes (start) allows you to span
multiple lines.  For example:
ax^2 + bx + c is a polynomial

Problem second question
ANSWER HERE:

To end the comment, we repeat the triple quotes
'''

# Problem 4
# This is done for homework
#########################
# input P principle, n times a year, t years, r rate
# output money accrued 
def sinking_fund(P,n,t,r):
    rate_per_period = r / n
    growth = (1 + rate_per_period) ** (n * t)
    bracket = (growth - 1) / rate_per_period
    result = P * bracket
    result = round(result, 2)
    return result

data = [(2.2e4,1,7,6/100),(500,12,20,4/100),
        (1200,4,10,8/100)]

 
for d in data:
     print(sinking_fund(*d))
