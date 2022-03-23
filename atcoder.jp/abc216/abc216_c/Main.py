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
    tmp = n
    ans = []
    while tmp != 0:
        if tmp%2 == 0:
            tmp = tmp // 2
            ans.append('B')
        else:
            tmp-=1
            ans.append('A')
    ans.reverse()
    print(''.join(ans))