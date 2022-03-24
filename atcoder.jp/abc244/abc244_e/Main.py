def main():
    n,m,k,s,t,x = map(int, input().split())
    s-=1
    t-=1
    x-=1
    e = [[] for _ in range(n)]
    for _ in range(m):
        u,v = map(int, input().split())
        u-=1
        v-=1
        e[u].append(v)
        e[v].append(u)
    dp = [[[0 for _ in range(n)] for _ in range(k+1)] for _ in range(2)]
    dp[0][0][s] = 1
    for l in range(k):
        for i in range(n):
            if i == x:
                for chi in e[i]:
                    dp[1][l+1][i] += dp[0][l][chi]
                    dp[0][l+1][i] += dp[1][l][chi]
            else:
                for chi in e[i]:
                    dp[1][l+1][i] += dp[1][l][chi]
                    dp[0][l+1][i] += dp[0][l][chi]
            dp[0][l+1][i]%=998244353
            dp[1][l+1][i]%=998244353
    print(dp[0][k][t])

if __name__ == '__main__':
    main()
