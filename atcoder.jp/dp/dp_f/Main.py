sr = lambda: input()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))


inf = 10 ** 18
mod = 10 ** 9 + 7
# mod = 998244353

# Press the green button in the gutter to run the script.
if __name__=='__main__':
    s=sr()
    t=sr()
    dp = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)] # [長さ，どこから]

    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

    ans = []
    s_ind = len(s)
    t_ind = len(t)
    while s_ind >= 1 and t_ind >= 1:
        if s[s_ind-1] == t[t_ind-1]:
            ans.append(s[s_ind-1])
            s_ind-=1
            t_ind-=1
        elif dp[s_ind-1][t_ind] > dp[s_ind][t_ind-1]:
            s_ind-=1
        else:
            t_ind-=1
    ans.reverse()
    print(*ans, sep='')