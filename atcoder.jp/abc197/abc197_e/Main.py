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
    xc = [lr() for _ in range(n)]
    xc.sort(key=lambda x:x[1])
    c_lr = {}
    c_ind = 0
    c_now = xc[0][1]
    now_max = xc[0][0]
    now_min = xc[0][0]
    for x,c in xc:
        if c_now == c:
            now_max = max(x, now_max)
            now_min = min(x, now_min)
        else:
            c_lr[c_ind]=[now_min, now_max]
            c_ind+=1
            c_now=c
            now_max=x
            now_min=x
    c_lr[c_ind]=[now_min, now_max]
    c_lr[-1]=[0, 0]
    c_ind+=1
    c_lr[c_ind]=[0, 0]
    c_num = c_ind+1

    dp = [[inf for j in range(2)] for i in range(c_num+1)]
    dp[0][0] = 0
    dp[0][1] = 0
    for i in range(c_num):
        l_p=c_lr[i][0]
        r_p=c_lr[i][1]
        now_c = dp[i][0]
        now_p = c_lr[i-1][0]
        dp[i+1][0] = now_c + abs(now_p-r_p)+r_p-l_p
        dp[i+1][1] = now_c + abs(now_p-l_p)+r_p-l_p
        now_c = dp[i][1]
        now_p = c_lr[i-1][1]
        dp[i+1][0] = min(now_c + abs(now_p-r_p)+r_p-l_p, dp[i+1][0])
        dp[i+1][1] = min(now_c + abs(now_p-l_p)+r_p-l_p, dp[i+1][1])

    ans = min(dp[c_num][0], dp[c_num][1])
    print(ans)
