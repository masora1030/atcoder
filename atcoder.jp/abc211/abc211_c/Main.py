sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
mod=10**9+7
# mod = 998244353

if __name__=='__main__':
    s=sr()
    dp = [[0 for j in range(9)] for i in range(len(s)+1)]
    dic = {'c':1, 'h':2, 'o':3, 'k':4, 'u':5, 'd':6, 'a':7, 'i':8}
    dp[0][0] = 1
    for i in range(len(s)):
        for j in range(9):
            dp[i+1][j] = dp[i][j]
        if s[i] in dic:
            ind = dic[s[i]]
            dp[i+1][ind]+=dp[i][ind-1]
            dp[i+1][ind]%=mod
    print(dp[len(s)][8])