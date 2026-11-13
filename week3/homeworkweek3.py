# C200 Fall 2026, Week 3 Homework
# Submit this file to Assignment 3 on Canvas (Assignments > Assignment 3)
# by Wednesday, Sept 23 at 9:00 PM EST.
# Do not rename this file, its functions, or their parameters.

#round to 2 decimal places
#input t years = 0, 1, then 2
#output dollars
def h_0(t):
    return 110 / ((1/2) * t + 1)
    
def h_1(t):
    return 26 * ((1/4)*t**2 - 1)**2 + 52

def h(t):
    if 0 <= t <= 2:
        return round (h_0(t) - h_1(t), 2)
    else:
        return -1

for d in 0,1,1.5,2,3:
     print(d,h(d))

#problem 2
#input P home price, r rate, n payments per year
#      t term (years), PMI rate PMI_rate, 
#      down payment down_payment
#output monthly paymet that takes into account PMI
def cost(P,r,n,t,PMI_rate,down_payment):
    R = r/100 / 12
    N = n * t
    Pd = P - down_payment
    PMT = Pd * R * (1 + R)**N / ((1 + R)**N - 1)
    if down_payment/P < 0.2:
        PMI = PMI_rate*P/12
        return round (PMT + PMI,2)
    else:
        return round (PMT,2)

home_price, rate = 4.15e5, 7
term,n = 30,12
down_payment = 0
data = [(0,0),(0,1.5/100),(home_price*.10,1.5/100),(home_price*.20,1.5/100)]

print("${:<15}    ${:<15}".format("down pmt","monthly pmt"))
for down_payment, PMI_rate in data:
    print("{:<15}     {:<15}".format(down_payment, cost(home_price,rate,term,n,PMI_rate,down_payment)))                  


# problem 3
# input ax + by > c, coefficients a,b,c
# point = (x,y)
# true,false depending on inequality
def linear_query(a,b,c,point):
    x,y = point
    return a*x + b*y > c

point1 = (-6,0)
point2 = (4,-5)
print(point1, linear_query(3,-4,12,point1))
print(point2, linear_query(3,-4,12,point2))

# problem 4
# input earth_time time on earth
# output time we experienced traveling
def time_contract(earth_time):
    c = 186000
    v = .9 * c
    return round(earth_time * (1 - (v/c)**2)**(1/2),2)

earth_times = [1,25,50,75]

for et in earth_times:
    print(time_contract(et))


# problem 5
# input taxable income as income
# output amount of federal tax owed
def tax_payment(income):
    if income < 12401:
        rate = 10
    elif income < 50401:
        rate = 12
    elif income < 105701:
        rate = 22
    elif income < 201776:
        rate = 24
    elif income < 256226:
        rate = 32
    elif income < 640601:
        rate = 35
    else:
        rate = 37
    return round(income * rate / 100, 2)
        

incomes = [10000,30000,100000,200000,250000,400000,700000]
for i in incomes:
    print(i, tax_payment(i))
