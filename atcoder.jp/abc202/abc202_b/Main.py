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
    s=list(sr())
    dic = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    s.reverse()
    ans = []
    for c in s:
        ans.append(dic[c])
    print(''.join(ans))
