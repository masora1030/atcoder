from sys import stdin
readline = stdin.readline
sr = lambda: readline()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

inf = 10 ** 18
# mod = 10 ** 9 + 7
mod = 998244353
# len(bin(n)) - bin(n).rfind("1") - 1


if __name__=='__main__':
    h,w,k= lr()
    v = [[0 for kk in range(w)] for i in range(h)]
    for i in range(k):
        y,x,q = lr()
        y-=1
        x-=1
        v[y][x] = q
    dp = [[[0 for kk in range(w+1)] for i in range(h+1)] for j in range(4)]
    for i in range(h):
        for j in range(w):
            m=max(dp[0][i][j+1], dp[1][i][j+1], dp[2][i][j+1], dp[3][i][j+1])
            dp[0][i+1][j+1] = max(dp[0][i+1][j], m)
            tmp=v[i][j]
            if tmp > 0:
                dp[1][i+1][j+1]=max(dp[1][i+1][j], dp[0][i+1][j]+tmp, m+tmp)
                dp[2][i+1][j+1]=max(dp[2][i+1][j], dp[1][i+1][j]+tmp)
                dp[3][i+1][j+1]=max(dp[3][i+1][j], dp[2][i+1][j]+tmp)
            else:
                dp[1][i+1][j+1]=dp[1][i+1][j]
                dp[2][i+1][j+1]=dp[2][i+1][j]
                dp[3][i+1][j+1]=dp[3][i+1][j]

    print(max(dp[0][h][w], dp[1][h][w], dp[2][h][w], dp[3][h][w]))