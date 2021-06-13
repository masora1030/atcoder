import sys
import bisect

# sys.setrecursionlimit(10**4)
# from sys import stdin
# readline = stdin.readline
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
mod=10**9+7
# mod = 998244353

# ダイクストラで始点からの各ノードへのコストを返す (eという配列にstart:[[dist, end], [dist, end]]というエッジを格納)

if __name__=='__main__':
    n=ir()
    a=lr()
    a.sort()
    flg = True
    for i in range(n):
        if a[i] != i+1:
            flg = False
            break
    if flg:
        print("Yes")
    else:
        print("No")