import math


#problme 0

#INPUT n0 start colony size, m growth rate, t time
#RETURN final colony size
def N(n_0, m, t):
    return n_0 * math.exp(m*t)

print(N(500, 100, 4))

#INPUT t days
#RETURN number of teeth
def N_t(t):
    return math.ceil(71.8 * math.exp(-8.96 * math.exp(-0.0685 * t)))

print(N_t(1000))

#INPUT pressures Pi, Pf 
#RETURN work joules
def W(P_i, P_f):
    return math.ceil(8.314 * 300 * math.log(P_i / P_f))

print(W(10,1))


#INPUT V miles per hour, A area, C_l lift coefficient
#RETURN lbs 
def L(V,A,C_l):
    return math.ceil(0.0033 * V**2 * A * C_l)

print(L(33.8, 512, 0.515))



#problem 1
def remove_all(x,lst):
    return [item for item in lst if item != x]

d1 = [(1,[]),(1,[2]),(1,[1,1,1,3,1,1]),(2,[[2]])]

for d in d1:
    print(remove_all(*d))

#problem 2
def remove_less_or_equal_to(x,lst):
    return [item for item in lst if item > x]

d2 = [(1,[]),(1,[1]), (1,[0,1,2]),(1,[2,3,4,5])]
for d in d2:
    print(remove_less_or_equal_to(*d))

#problem 3
def consecutive(p,lst):
    count = 0
    for i in range(len(lst) - 1):
        if lst[i] == p[0] and lst[i + 1] ==p [1]:
            count += 1
    return count

d3 = [((1,2),[]),((1,2),[2]),((1,2),[1,2]),((1,2),[1,2,2,1,2,1,2,2])]
for d in d3:
     print(consecutive(*d))

# problem 4
def f_1(x):
    return x**2 - 1

def f_2(x):
    return (0.8 * x + 1000) / (5 * x + 4)

def arc(f,p):
    return round((f(p[1]) - f(p[0])) / (p[1] - p[0]), 2)

print(arc(f_1,(1,3)))
print(arc(f_2,(1,3)))


#problem 5
def brush_be_gone(w):
    return 32 + 0.2 * (w - 100)

print(brush_be_gone(100))
print(brush_be_gone(180))

print(arc(brush_be_gone,(180,100)))

# problem 6
def c(t):
    return round(20 * (math.exp(-t) - math.exp(-2 * t)), 3)

def check_drug(data):
    result = []
    for time, conc in data:
        correct = c(time)
        if conc != correct:
            result.append((time, conc, correct))
    return result

data = [(1, 4.651),(2, 2.14),(3, 0.946),(4, 1.36),(5, 0.134), (6, 0.051), (7, 0.018), (8, 0.008),(9, 0.002),(10, 0.001),(11,.001)]
print(check_drug(data))


#problem 7
#INPUT [name0,name1, votes] where votes is a non-empty list of 0,1
#RETURN a tuple (name, c, t) where name is the winner, c is the number of winning votes
#t is the total votes cast 
def decision(data):
    name0, name1, votes = data
    total = len(votes)
    ones = sum(votes)
    zeros = total - ones
    if zeros > ones:
        return (name0, zeros, total)
    elif ones > zeros:
        return (name1, ones, total)
    else:
        return ('tie', zeros, zeros)

data0 = ['B','Z',[0,1,1,0,1,0,0]]
print(decision(data0))
data1 = ['B', 'Z',[1,0,1]]
print(decision(data1))
data2 = ['B', 'Z',[1,0,1,0,1,1,0,0]]
print(decision(data2))

# problem 8

err_msg = ["Data Error: 0 values", "Data Error: 0 in data"]

def arithmetic_mean(nlst):
    if len(nlst) == 0:
        return err_msg[0]
    return sum(nlst) / len(nlst)

def geo_mean(nlst):
    if len(nlst) == 0:
        return err_msg[0]
    total = 0
    for x in nlst:
        total += math.log10(x)
    return 10 ** (total / len(nlst))

def har_mean(nlst):
    if len(nlst) == 0:
        return err_msg[0]
    if 0 in nlst:
        return err_msg[1]
    total = 0
    for x in nlst:
        total += 1 / x
    return len(nlst) / total
    
def RMS_mean(nlst):
    if len(nlst) == 0:
        return err_msg[0]
    total = 0
    for x in nlst:
        total += x ** 2
    return math.sqrt(total / len(nlst))

print(arithmetic_mean([]))
print(arithmetic_mean([1,2,3]))
print(geo_mean([]))
print(geo_mean([2,4,8]))
print(har_mean([]))
print(har_mean([1,2,3]))
print(har_mean([1,2,0]))
print(RMS_mean([1,3,4,5,7]))

# problem 9
def loan(cr, lst):
    result = []
    for name, cd in lst:
        score = 0.35*cd['P'] + 0.30*cd['A'] + 0.15*cd['L'] + 0.10*cd['N'] + 0.10*cd['C']
        if score >= cr:
            result.append([name, score])
    return result

data9 = [['x',{'P':600, 'L':700,'A': 500, 'N': 170, 'C': 250}],
        ['y',{'P':550, 'L':720,'A': 500, 'N': 230, 'C': 250}],
        ['b',{'P':560, 'L':710,'A': 500, 'N': 221, 'C': 250}],
        ['c',{'P':800, 'L':700,'A': 200, 'N': 100, 'C': 150}],
        ['a',{'P':800, 'L':800,'A': 600, 'N': 250, 'C': 150}],
        ['z',{'P':800, 'L':800,'A': 500, 'N': 250, 'C': 150}]]
print(loan(550,data9))
