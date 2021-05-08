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
    a=lr()
    if n == 1:
        print("No")
        sys.exit()
    dp = [[[] for j in range(200)] for i in range(n+1)]
    dp[0][0] = [0]
    flg = False
    for i in range(n):
        num = a[i]%200
        for j in range(200):
            if dp[i][j] and dp[i][(j-num)%200]:
                b = dp[i][j].copy()
                dp[i][(j-num)%200].append(i+1)
                c = dp[i][(j-num)%200].copy()
                dp[i][(j-num)%200].pop()
                if j == 0 and not flg:
                    flg = True
                    dp[i+1][j] = c.copy()
                    continue
                print("Yes")
                # b = deque(b)
                # c = deque(c)
                # b.appendleft(len(b))
                # c.appendleft(len(c))
                b[0] = len(b)-1
                c[0] = len(c)-1
                print(*b, sep=" ")
                print(*c, sep=" ")
                sys.exit()
            elif dp[i][j]:
                dp[i+1][j] = dp[i][j].copy()
            elif dp[i][(j-num)%200]:
                dp[i][(j-num)%200].append(i+1)
                dp[i+1][j] = dp[i][(j-num)%200].copy()
                dp[i][(j-num)%200].pop()
    print("No")