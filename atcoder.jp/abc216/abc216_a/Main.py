sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

import sys

inf=10**18
# mod = 10**9+7
mod=998244353

if __name__=='__main__':
    x,y = map(int, input().split('.'))
    if 0 <= y <= 2:
        print(f"{x}-")
    elif y <= 6:
        print(f"{x}")
    else:
        print(f"{x}+")
