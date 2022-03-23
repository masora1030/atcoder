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
    n = ir()
    dic = {}
    flg = False
    for i in range(n):
        s = sr()
        if s in dic:
            flg = True
            break
        dic[s] = 1
    if flg:
        print("Yes")
    else:
        print("No")