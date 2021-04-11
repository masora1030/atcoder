import sys
# from sys import stdin
# readline = stdin.readline
sr = lambda: input()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

import bisect

from sys import stdout

inf = 10 ** 18
# mod = 10 ** 9 + 7
mod = 998244353
# len(bin(n)) - bin(n).rfind("1") - 1

import random

if __name__=='__main__':
    r,x,y = lr()
    total = (x**2 + y**2)**(1/2)
    int_total = int(total)
    if int_total**2 == x**2 + y**2 and int_total%r == 0:
        print(int_total//r)
    else:
        tmp=int((total)//r)
        if tmp == 0:
            print(2)
        else:
            print(tmp+1)