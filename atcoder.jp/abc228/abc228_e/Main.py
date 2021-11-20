sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    n,k,m = lr()
    if m%mod == 0:
        print(0)
    else:
        ans = pow(m%mod,pow(k,n,mod-1),mod)
        print(ans)