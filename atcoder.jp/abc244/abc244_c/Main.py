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
    n=ir()
    ret = [i for i in range(1,2*n+2)]
    while ret:
        t = ret.pop()
        print(t)
        sys.stdout.flush()
        a = ir()
        ret.remove(a)
    print(0)
