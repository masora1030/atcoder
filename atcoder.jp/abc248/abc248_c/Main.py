sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    n,m,k = lr()
    dp=[[0 for _ in range(k+1)] for _ in range(n+1)]
    dp[0][0]=1
    for i in range(n):
        for j in range(1,m+1):
            for l in range(k+1):
                if l+j <= k:
                    dp[i+1][l+j]+=dp[i][l]
                    dp[i+1][l+j]%=mod
    print(sum(dp[n])%mod)


if __name__ == '__main__':
    main()
