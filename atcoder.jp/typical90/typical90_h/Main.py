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
    n=ir()
    s=sr()
    ss='atcoder'
    c_to_ind={c:i for i,c in enumerate(list(ss))}
    dp = [[0 for _ in range(7)] for i in range(n+1)]
    for i in range(n):
        c = s[i]
        for j in range(7):
            dp[i+1][j] = dp[i][j]
        if c in c_to_ind:
            ind = c_to_ind[c]
            if ind == 0:
                dp[i+1][ind]+=1
            else:
                dp[i+1][ind]+=dp[i][ind-1]
        for j in range(7):
            dp[i+1][j]%=mod
    print(dp[n][6])