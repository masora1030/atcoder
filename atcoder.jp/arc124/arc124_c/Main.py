import sys
import bisect
from collections import deque
import itertools
import math
import heapq
import random

# sys.setrecursionlimit(10**4)
from sys import stdin
# readline = stdin.readline
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    n=ir()
    # for i in range(n):
    #     x,y = lr()
    #     a.append([factorization(x), factorization(y)])
    # for x,y in a:
    #     print(x)
    #     print(y)
    #     print('---------------')
    # print(factorization(238630))
    aa = [lr() for i in range(n)]
    random.shuffle(aa)
    a,b = aa[0]
    for i in range(n-1):
        x,y = aa[i+1]
        tmp1 = math.gcd(a,x)
        tmp2 = math.gcd(a,y)
        tmp3 = math.gcd(b,x)
        tmp4 = math.gcd(b,y)
        if tmp1*tmp4//math.gcd(tmp1, tmp4) > tmp2*tmp3//math.gcd(tmp2, tmp3):
            a = tmp1
            b = tmp4
        else:
            a = tmp2
            b = tmp3
    print(a*b//math.gcd(a,b))