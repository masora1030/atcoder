# import sys
# sys.setrecursionlimit(10**6)
from sys import stdin
# readline = stdin.readline
# sr=lambda: readline()
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    k=ir()
    a,b = input().split()
    a = list(a)
    b = list(b)
    a.reverse()
    b.reverse()
    na = 0
    nb = 0
    tmp = 1
    for num in a:
        nu = int(num)
        na+=tmp*nu
        tmp*=k
    tmp = 1
    for num in b:
        nu = int(num)
        nb+=tmp*nu
        tmp*=k
    print(na*nb)

