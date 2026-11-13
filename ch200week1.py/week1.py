# <Ty Rosenbaum> <tydrosen@iu.edu>
# C/H200 Fall 2026 Dalkilic
# free use of code with acknowledgement
# week 1 homework

import math

# volume of cone
# input radius r, height h
# output volume 
def c(r,h):
    _c = (1/3) * math.pi * (r**2) * h
    return _c

data = [(2,5),(3,7)]
for d in data:
    print(d, c(*d))

# model of flu outbreak
# input S is number of healthy, but susceptible children
# output number of infected 
def I(S):
    A,B,C = 192,762,763

    _s = math.ceil(A*math.log2(S/B) - S + C)

    return _s

data = [100,300]
for d in data:
    print(d,I(d))

# model of pitcher
# input earned runs, innings
# output ERA
def ERA(e,i):
    max_outs = 3.0
    _era = 0
    whole_innings = int(i)

    outs = round((i - whole_innings) * 10)

    true_innings = whole_innings + (outs/max_outs)

    if true_innings:
        _era = round((e * 9)/true_innings,2)

    return _era

data = [("Jackson Flora",8, 69.1), 
        ("Mason Edwards", 22, 95.2),
        ("Ben Blair", 30, 77.1)]

for name,e,i in data:
    print(name, ERA(e,i))
