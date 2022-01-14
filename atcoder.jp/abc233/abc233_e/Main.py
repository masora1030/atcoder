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
    x = list(sr())
    x.reverse()
    total = 0
    dp = [0 for i in range(len(x)+10)]
    ans = [0 for i in range(len(x)+10)]
    for c in x:
        tmp = int(c)
        total += tmp
    now_ind = 0
    for i,c in enumerate(x):
        tmp = int(c)
        init = total+dp[i]
        ans[i] = init % 10
        total-=tmp
        now_ind+=1
        init //= 10
        str_init = list(str(init))
        str_init.reverse()
        for j in range(len(str_init)):
            dp[now_ind+j] += int(str_init[j])
    for ind in range(now_ind, len(x)+10):
        ans[ind] = dp[ind]
    ans.reverse()
    ind = 0
    while ans[ind] == 0 and ind < len(ans):
        ind+=1
    print(*ans[ind:], sep='')
