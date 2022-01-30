sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

import sys

inf = 10**18
# mod = 10**9+7
mod = 998244353

if __name__=='__main__':
    h,w = lr()
    a = [lr() for i in range(h)]
    ans = [[-1 for j in range(h)] for i in range(w)]
    for i in range(h):
        for j in range(w):
            ans[j][i] = a[i][j]
    for ll in ans:
        print(*ll, sep=' ')