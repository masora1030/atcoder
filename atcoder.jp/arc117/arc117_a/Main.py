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
    a,b = lr()
    ans = []
    if a>=b:
        for i in range(a):
            ans.append(i+1)
        for j in range(b-1):
            ans.append(-(j+1))
        ans.append(-(a+b)*(a-b+1)//2)
    else:
        for i in range(b):
            ans.append(-(i+1))
        for j in range(a-1):
            ans.append(j+1)
        ans.append((a+b)*(b-a+1)//2)
    print(*ans, sep=' ')