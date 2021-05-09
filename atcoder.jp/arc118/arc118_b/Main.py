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
    k,n,m = lr()
    a = lr()
    ans = [0 for i in range(k)]
    gosa = [[0, i] for i in range(k)]
    for i,num in enumerate(a):
        ans[i] = int(num*m/n)
        gosa[i][0] = num*m/n - ans[i]
    total = sum(ans)
    ret = m - total
    gosa.sort(reverse=True)
    for i in range(ret):
        ans[gosa[i][1]]+=1
    print(*ans, sep=' ')