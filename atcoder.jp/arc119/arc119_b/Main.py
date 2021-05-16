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

if __name__=='__main__':
    n = ir()
    s = sr()
    t = sr()
    counts = 0
    countt = 0
    inds = []
    indt = []
    for i in range(n):
        if s[i] == '0':
            counts+=1
            inds.append(i)
        if t[i] == '0':
            countt+=1
            indt.append(i)
    if counts != countt:
        print(-1)
    else:
        ans = 0
        for i in range(counts):
            if inds[i] != indt[i]:
                ans+=1
        print(ans)