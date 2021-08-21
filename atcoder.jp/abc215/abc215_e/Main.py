sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    n=ir()
    s=sr()
    max_group = 2**10
    bekis = [1]
    for i in range(9):
        bekis.append(bekis[-1]*2)
    dp=[[[0 for k in range(10)] for j in range(max_group)] for i in range(n+1)]
    for k in range(10):
        dp[0][0][k] = 1
    for i in range(n):
        now = ord(s[i]) - ord('A')
        for j in range(max_group):
            for k in range(10):
                dp[i+1][j][k] = dp[i][j][k]
            now_flg = False
            for tmp in range(10):
                if (j >> tmp) & 1:
                    if tmp == now:
                        now_flg = True
                        break
            if now_flg:
                if j-bekis[now] > 0:
                    for k in range(10):
                        dp[i+1][j][now] += dp[i][j-bekis[now]][k]
                    dp[i+1][j][now] += dp[i][j][now]
                else:
                    dp[i+1][j][now] += dp[i][j-bekis[now]][now]
                    dp[i+1][j][now] += dp[i][j][now]
                dp[i+1][j][now]%=mod
    ans = 0
    for j in range(1,max_group):
        for k in range(10):
            ans += dp[n][j][k]
        ans%=mod
    print(ans)

