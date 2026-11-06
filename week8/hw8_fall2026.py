import math
import numpy as np

########################
# PROBLEM 1
########################

#recursive functions
def p(n):
    if n == 0:
        return 10000
    return p(n - 1) + 0.02 * p(n - 1)

def c(n):
    if n == 1:
        return 9
    return 9 * c(n - 1) + 10 ** (n - 1) - c(n - 1)

def d(n):
    if n == 0:
        return 1
    return 3 * d(n - 1) + 1

def f(n):
    if n == 0 or n == 1:
        return 1
    return f(n - 1) + f(n - 2)
 
def e(n):
    if n == 1:
        return 12
    return -5 * e(n - 1)

def M(c,i):
    if c == 0:
        return 1
    if c < 0 or f(i) > 10:
        return 0
    return M(c - f(c), i + 1) + M(c, i + 1)
    
def c_2(n,k):
    if k == 0 or k == n:
        return 1
    return c_2(n - 1, k - 1) + c_2(n - 1, k)
    

########################
# PROBLEM 2
########################
      
def m(lst):
    if len(lst) == 1:
        return []
    if len(lst) == 2:
        return [[lst[0] + lst[1]]]
    row = [lst[i] + lst[i + 1] for i in range(len(lst) - 1)]
    return [row] + m(row)


########################
# PROBLEM 3
########################

def encode(msg,shift):
    result = ""
    for ch in msg:
        idx = 26 if ch == " " else ord(ch) - ord("a")
        new_idx = (idx + shift) % 27
        result += chr(new_idx + ord("a"))
    return result

def decode(msg,shift):
    result = ""
    for ch in msg:
        idx = ord(ch) - ord("a")
        new_idx = (idx - shift) % 27
        result += " " if new_idx == 26 else chr(new_idx + ord("a"))
    return result

########################
# PROBLEM 4
########################
def prod(lst):
    if len(lst) == 0:
        return 1
    return lst[0] * prod(lst[1:])
    
def tr_prod(lst,c=1):
    if len(lst) == 0:
        return c
    return tr_prod(lst[1:], c * lst[0])

def pal(xstr):
    if len(xstr) <= 1:
        return True
    if xstr[0] != xstr[-1]:
        return False
    return pal(xstr[1:-1])

    
def tr_pal(xstr,c=True):
    if not c:
        return False
    if len(xstr) <= 1:
        return c
    return tr_pal(xstr[1:-1], xstr[0] == xstr[-1])

def loc(x,lst,i=0):
    if i >= len(lst):
        return []
    rest = loc(x, lst, i + 1)
    if lst[i] == x:
        return [i] + rest
    return rest
    
def tr_loc(x,lst,i=0,c=[]):
    if i >= len(lst):
        return c
    if lst[i] == x:
        return tr_loc(x, lst, i + 1, c + [i])
    return tr_loc(x, lst, i + 1, c)

########################
# PROBLEM 5
########################
def prime(p):
    if p < 2:
        return False
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False
    return True

########################
# PROBLEM 6
########################
def sin_(x,n):
    total = 0
    for k in range(n + 1):
        total += ((-1) ** k) * x ** (2 * k + 1) / math.factorial(2 * k + 1)
    return total

if __name__ == "__main__":

    """
    write tests here...
    do not remove this comment
    this will not be used by Gradescope
    """

    # ## Problem 1
    # # you should see these values
    # p(0) = 10000
    # p(1) = 10200.0
    # p(2) = 10404.0
    # p(3) = 10612.08
    # p(4) = 10824.3216
    for i in range(5):
         print(p(i))
 
    
    for i in range(2,6):
         print(c(i))
    print(c(1))
    # # you should see these values
    # c(2) = 82
    # c(3) = 756
    # c(4) = 7048
    # c(5) = 66384    

    for i in range(5):
         print(d(i))
    # # you should see these values
    # d(0) = 1
    # d(1) = 4
    # d(2) = 13
    # d(3) = 40
    # d(4) = 121
    
    for i in range(6):
         print(f(i))
    # # you should see these values
    # f(0) = 1
    # f(1) = 1
    # f(2) = 2
    # f(3) = 3
    # f(4) = 5
    # f(5) = 8

    for i in range(1,6):
         print(e(i))
    # # you should see these values
    # e(1) = 12
    # e(2) = -60
    # e(3) = 300
    # e(4) = -1500
    # e(5) = 7500

    for i in range(5):
         for j in range(5):
             print(M(i,j), " ", end="")
    # # you should see these values
    # M((0, 0)) = 1
    # M((0, 1)) = 1
    # M((0, 2)) = 1
    # M((0, 3)) = 1
    # M((0, 4)) = 1
    # M((1, 0)) = 6
    # M((1, 1)) = 5
    # M((1, 2)) = 4
    # M((1, 3)) = 3
    # M((1, 4)) = 2
    # M((2, 0)) = 6
    # M((2, 1)) = 5
    # M((2, 2)) = 4
    # M((2, 3)) = 3
    # M((2, 4)) = 2
    # M((3, 0)) = 6
    # M((3, 1)) = 5
    # M((3, 2)) = 4
    # M((3, 3)) = 3
    # M((3, 4)) = 2
    # M((4, 0)) = 0
    # M((4, 1)) = 0
    # M((4, 2)) = 0
    # M((4, 3)) = 0
    # M((4, 4)) = 0    

    for i in range(2,6):
          print(c_2(5,i))
    # # # you should see these values
    # c_2(5,2) = 10
    # c_2(5,3) = 10
    # c_2(5,4) = 5
    # c_2(5,5) = 1

    # # problem 2
    data2 = [[1,2,3,4,5],[1],[3,4],[5,10,22],[1,2,3,4,5,6]]
    for d in data2:
          print(m(d))
    
    # #problem 3
    data3 = ["abc xyz","the cat", "i love ctwohundred"]
    for i,j in enumerate(data3,start=2):
          print(f"original msg {j}")
          print(f"encoded  msg {encode(j,i)}")
          print(f"decoded  msg {decode(encode(j,i),i)}")
    secret_msg = encode("the quick brown fox jumps over the lazy dog", 24)
    print(secret_msg)
    print(decode(secret_msg,24))

    # #problem 4
    
    data4_1 = [[],[1,5,3],[0],[i for i in range(1,5)]]
    for d in data4_1:
            print(prod(d),tr_prod(d)) 

    
    data4_2 = ["","1","22","23","121","122"]
    for d in data4_2:
         print(pal(d),tr_pal(d))

    data4_3 = [[1,[]],[1,[1,2,1]],[2,[1,1,1,4]],[1,[1,1,1,1,1]]]
    for d in data4_3:
         print(loc(*d),tr_loc(*d))


    # #problem 5
    ps5 = []
    for p in range(2,100):
        if prime(p):
            ps5.append(p)
    print(ps5)

    # # problem 6
    print(math.sin(4),sin_(4,20))
    print(math.sin(2),sin_(2,4))
    print(math.sin(1.4),sin_(1.5,30))