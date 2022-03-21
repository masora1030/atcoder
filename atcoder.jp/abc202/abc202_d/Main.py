sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

import sys

from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

inf=10**18
# mod = 10**9+7
mod=998244353

if __name__=='__main__':
    a,b,k = lr()
    def get_str(x,y,ret):
        if x == 0:
            return ['b' for _ in range(y)]
        if y == 0:
            return ['a' for _ in range(x)]
        ans = []
        now_num = 0
        pre_num = 0
        for i in range(x+1):
            tmp = cmb(y-1+i, i)
            pre_num = now_num
            now_num += tmp
            if ret > now_num:
                continue
            for j in range(x-i):
                ans.append('a')
            ans.append('b')
            ll = get_str(i,y-1,ret-pre_num)
            for c in ll:
                ans.append(c)
            break
        return ans
    print(''.join(get_str(a,b,k)))