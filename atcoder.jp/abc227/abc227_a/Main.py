sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

# import numpy as np

if __name__=='__main__':
    n,k,a = lr()
    if (k+a-1)%n == 0:
        print(n)
    else:
        print((k+a-1)%n)
