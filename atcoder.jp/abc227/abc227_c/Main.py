sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

# import numpy as np

if __name__=='__main__':
    n=ir()
    ans = 0
    for a in range(1, int(n**(1/3))+2):
        if a*a*a > n:
            continue
        ret = n//a
        for b in range(a, int(ret**(1/2))+2):
            if b*b > ret:
                continue
            ans+=(ret//b-b+1)
    print(ans)
