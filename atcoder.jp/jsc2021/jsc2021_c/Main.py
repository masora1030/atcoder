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
    a,b = lr()
    ans = 1
    for num in range(1, (b-a)+1):
        tmp = a//num
        if a%num != 0:\
            tmp+=1
        if (tmp+1)*num <= b:
            ans = max(ans, num)
    print(ans)