inf = 10**15
mod = 10**9+7

h,w,k = list(map(int, input().split()))
# 高さiの時jにいる通り
dp = [[0 for j in range(w+1)]for i in range(h+1)]
dp[0][1] = 1
for i in range(h):
    for x in range(2**(w-1)):
        flag = True
        count = 0
        tmp = x
        for l in range(w-1):
            if ((tmp >> l) & 1):
                count+=1
                if count == 2:
                    flag = False
            else:
                count=0
        if flag:
            zeroflag = True
            for j,y in enumerate(range(w-1)):
                if ((x >> y) & 1):  # 1だったら(オンだったら)
                    dp[i+1][j+1] += dp[i][j+2]
                    dp[i+1][j+2] += dp[i][j+1]
                    zeroflag = False
                else:
                    if zeroflag:
                        dp[i+1][j+1] += dp[i][j+1]
                    else:
                        zeroflag = True
            if zeroflag:
                dp[i+1][-1] += dp[i][-1]
    for g in range(1,w+1):
        dp[i+1][g] = dp[i+1][g] % mod
print(dp[h][k])