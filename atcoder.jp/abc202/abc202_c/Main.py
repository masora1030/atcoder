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
    a=lr()
    b=lr()
    c=lr()
    b_dic = {}
    for ind in c:
        ind-=1
        num = b[ind]
        if num in b_dic:
            b_dic[num]+=1
        else:
            b_dic[num]=1
    ans = 0
    for num in a:
        if num in b_dic:
            ans += b_dic[num]
    print(ans)
