import sys
import bisect

# sys.setrecursionlimit(10**4)
# from sys import stdin
# readline = stdin.readline
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    n=ir()
    a=lr()
    ans = 0
    for num in a:
        if num >= 10:
            ans+=(num-10)
    print(ans)