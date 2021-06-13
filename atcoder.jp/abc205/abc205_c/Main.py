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
    a,b,c = lr()
    if c%2 == 0:
        if abs(a) > abs(b):
            print(">")
        elif abs(a) == abs(b):
            print("=")
        else:
            print("<")
    else:
        if a >= 0 and b >= 0:
            if abs(a)>abs(b):
                print(">")
            elif abs(a)==abs(b):
                print("=")
            else:
                print("<")
        elif a >= 0 and b < 0:
            print(">")
        elif a < 0 and b >= 0:
            print("<")
        else:
            if abs(a)>abs(b):
                print("<")
            elif abs(a)==abs(b):
                print("=")
            else:
                print(">")