import sys
# sys.setrecursionlimit(10**4)
# from sys import stdin
# readline = stdin.readline
sr = lambda: input()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

import bisect

from sys import stdout

inf = 10 ** 18
mod = 10 ** 9 + 7
# mod = 998244353
# len(bin(n)) - bin(n).rfind("1") - 1

import random

if __name__=='__main__':
    n=ir()
    a=lr()
    dic = {}
    for num in a:
        dic[num] = 0
    num_list = sorted(dic.keys())
    pre = 0
    ans = 1
    for num in num_list:
        ans = (ans*(num-pre+1))%mod
        pre=num
    print(ans)