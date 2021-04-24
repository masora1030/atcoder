import sys

# sys.setrecursionlimit(10**4)
# from sys import stdin
# readline = stdin.readline
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

import bisect

from sys import stdout

inf=10**18
mod=10**9+7
# mod = 998244353
# len(bin(n)) - bin(n).rfind("1") - 1

import random


if __name__=='__main__':
    n = ir()
    s = list(sr())
    q = ir()
    flg = True
    for Q in range(q):
        t,a,b = lr()
        a-=1
        b-=1
        if t == 1:
            if flg:
                tmp = s[a]
                s[a] = s[b]
                s[b] = tmp
            else:
                if a<n:
                    a = a+n
                else:
                    a = a-n
                if b<n:
                    b=b+n
                else:
                    b=b-n
                tmp=s[a]
                s[a]=s[b]
                s[b]=tmp
        else:
            flg = not flg
    if flg:
        print(*s, sep='')
    else:
        ans = []
        for i in range(n, 2*n):
            ans.append(s[i])
        for i in range(n):
            ans.append(s[i])
        print(*ans, sep='')