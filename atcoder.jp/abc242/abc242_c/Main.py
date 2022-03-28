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
    dp=[[0]*n for _ in range(9)]
    for i in range(9):
        dp[i][0]=1
    for i in range(1,n):
        dp[0][i] += dp[0][i-1]
        dp[0][i] += dp[1][i-1]
        for j in range(1,8):
            dp[j][i] += dp[j-1][i-1]
            dp[j][i] += dp[j][i-1]
            dp[j][i] += dp[j+1][i-1]
        dp[8][i]+=dp[7][i-1]
        dp[8][i]+=dp[8][i-1]
        for j in range(9):
            dp[j][i] %= 998244353
    ans = 0
    for j in range(9):
        ans += dp[j][n-1]
    print(ans%998244353)


if __name__ == '__main__':
    main()
