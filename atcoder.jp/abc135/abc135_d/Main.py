s = str(input())
n = len(s)
MOD = 10**9 + 7

res_dic = {}
for i in range(13):
    if (i*10)%13 in res_dic:
        res_dic[(i*10)%13].append(i)
    else:
        res_dic[(i*10)%13] = [i]
        
caseq_list = [[0 for j in range(13)] for i in range(10)]
for num in range(10):
    for j in range(13):
        k = (j - num)%13
        if k in res_dic:
            for m in res_dic[k]:
                caseq_list[num][j] = m
        
dp = [[0 for j in range(13)] for i in range(n+1)]    # i番目までの文字を読み込んだ時に13で割った余りがjになる数の個数
if s[0] == '?':
    for i in range(10):
        dp[1][i] =  1
else:
    num = ord(s[0]) - ord('0')
    dp[1][num] = 1

for i in range(1,n):
    c = s[i]
    if c == '?':
        for num in range(10):
            for j in range(13):
                dp[i+1][j] = (dp[i+1][j] + dp[i][caseq_list[num][j]]) % MOD
    else:
        num = ord(c) - ord('0')
        for j in range(13):
            dp[i+1][j] = (dp[i+1][j] + dp[i][caseq_list[num][j]]) % MOD
print(dp[n][5])