import sys
import bisect
from collections import deque
import itertools
import math

# sys.setrecursionlimit(10**4)
from sys import stdin
# readline = stdin.readline
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
mod=10**9+7
# mod = 998244353

if __name__=='__main__':
    n,m=lr()
    ac={}
    for i in range(m):
        a,c=lr()
        if a in ac:
            ac[a] = min(ac[a], c)
        else:
            ac[a] = c
    flg = True
    acc = list(ac.items())
    gcd_now = math.gcd(n, acc[0][0])
    for k,_ in acc:
        gcd_now = math.gcd(gcd_now,k)
        if gcd_now == 1:
            flg = False
            break
    if flg:
        print(-1)
        sys.exit()
    acc.sort(key=lambda x:x[1])
    gcd_now = n
    ind = 0
    ans = 0
    while gcd_now != 1:
        pre = math.gcd(gcd_now,acc[ind][0])
        if pre < gcd_now:
            ans += (gcd_now-pre)*acc[ind][1]
            gcd_now = pre
        ind+=1
    print(ans)