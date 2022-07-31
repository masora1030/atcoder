sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353


def main():
    n=ir()
    a=lr()
    dp=[[[0 for k in range(n+1)] for j in range(n+1)] for i in range(n+1)] # i 個目まで見て k 個 使って j となる個数
    ans=0
    for m in range(1, n+1):
        dp[0][0][0] = 1
        for i in range(n):
            now_a = a[i]%m
            for j in range(m):
                for k in range(m+1):
                    dp[i+1][j][k] = dp[i][j][k]
            for j in range(m):
                for k in range(m):
                    dp[i+1][(j+now_a)%m][k+1] += dp[i][j][k]
                    dp[i+1][(j+now_a)%m][k+1] %= mod
        ans+=dp[n][0][m]
    print(ans%mod)

if __name__=='__main__':
    main()
