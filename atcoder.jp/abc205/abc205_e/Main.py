import sys
import bisect


# nCr

def ruijo(n, l, mod):
    a=n
    tmp=n-1
    while (tmp>=l):
        a=a*tmp%mod
        tmp-=1
    return a


def cmb(n, r, mod):
    if r==1:
        return n
    elif (n==r or r==0):
        return 1
    else:
        if (r<0 or r>n):
            return 0
        r=min(r, n-r)
        return ruijo(n, n-r+1, mod)*g2[r]%mod


mod=10**9+7  # 出力の制限
N=10**6*2
g1=[1, 1]  # 元テーブル
g2=[1, 1]  # 逆元テーブル
inverse=[0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, N+1):
    g1.append((g1[-1]*i)%mod)
    inverse.append((-inverse[mod%i]*(mod//i))%mod)
    g2.append((g2[-1]*inverse[-1])%mod)

# sys.setrecursionlimit(10**4)
# from sys import stdin
# readline = stdin.readline
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
mod=10**9+7
# mod = 998244353

if __name__=='__main__':
    n,m,k = lr()
    if n > m+k:
        print(0)
    else:
        print((cmb(n+m,n,mod)-cmb(n+m, m+k+1, mod))%mod)