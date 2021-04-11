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
    s = list(sr())
    while s and s[-1] == '0':
        s.pop()
    flg = True
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            flg = False
            break
    if flg:
        print("Yes")
    else:
        print("No")