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
    h,w = lr()
    a = [sr() for i in range(h)]
    score = [[0 for j in range(w)] for i in range(h)]
    dp=[[0 for j in range(w)] for i in range(h)]
    for i in range(h):
        for j in range(w):
            if a[i][j] == '+':
                if (i+j)%2 == 1:
                    score[i][j] = 1
                    dp[i][j]=-inf
                else:
                    score[i][j] = -1
                    dp[i][j]=inf
            else:
                if (i+j)%2 == 1:
                    score[i][j] = -1
                    dp[i][j]=-inf
                else:
                    score[i][j] = 1
                    dp[i][j]=inf
    if h == 1 and w == 1:
        print('Draw')
        sys.exit()
    dp[h-1][w-1] = 0
    for i in range(h):
        for j in range(w):
            sel = dp[h-1-i][w-1-j]-score[h-1-i][w-1-j]
            if ((h-1-i)+(w-1-j))%2 == 0:
                # 上と左のやつ(奇数)に向かって自分とのmaxをとる
                if 0<=(h-1-i-1)<=h-1:
                    dp[h-1-i-1][w-1-j] = max(sel, dp[h-1-i-1][w-1-j])
                if 0<=(w-1-j-1)<=w-1:
                    dp[h-1-i][w-1-j-1] = max(sel, dp[h-1-i][w-1-j-1])
            else:
                if 0<=(h-1-i-1)<=h-1:
                    dp[h-1-i-1][w-1-j] = min(sel, dp[h-1-i-1][w-1-j])
                if 0<=(w-1-j-1)<=w-1:
                    dp[h-1-i][w-1-j-1] = min(sel, dp[h-1-i][w-1-j-1])
    if dp[0][0] <= -1:
        print('Takahashi')
    elif dp[0][0] == 0:
        print('Draw')
    else:
        print('Aoki')