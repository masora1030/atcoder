sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    n,x,y=lr()
    r_dp = [0 for _ in range(n+1)]
    b_dp = [0 for _ in range(n+1)]
    r_dp[n]=1
    b_dp[n]=0
    for i in range(1,n):
        r_dp[n-i] = r_dp[n-i+1]*(x+1)+b_dp[n-i+1]
        b_dp[n-i] = r_dp[n-i+1]*(x*y)+b_dp[n-i+1]*y
    print(b_dp[1])

if __name__ == '__main__':
    main()
