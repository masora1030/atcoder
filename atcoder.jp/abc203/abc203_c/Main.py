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
    n,k = lr()
    ab = [lr() for i in range(n)]
    ab.sort()
    ret = k
    now = 0
    for a,b in ab:
        if now+ret < a:
            print(now+ret)
            sys.exit()
        else:
            ret = b+(ret-(a-now))
            now = a
    print(now+ret)
