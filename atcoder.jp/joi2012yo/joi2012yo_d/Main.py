# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
import sys
inf = 10**9+7
mod = 10**9+7

n,m = map(int, input().split())
dic = {}
for i in range(m):
    a,b = map(int, input().split())
    dic[a] = b
dp_t_safe = [0 for i in range(n+1)] # トマト
dp_t_dan = [0 for i in range(n+1)] # トマト
dp_c_safe = [0 for i in range(n+1)] # くりーむ
dp_c_dan = [0 for i in range(n+1)] # クリーム
dp_b_safe = [0 for i in range(n+1)] # バジル
dp_b_dan = [0 for i in range(n+1)] # バジル
if 1 in dic:
    if dic[1] == 1:
        dp_t_safe[1] = 1
    elif dic[1] == 2:
        dp_c_safe[1] = 1
    else:
        dp_b_safe[1] = 1
else:
    dp_t_safe[1] = 1
    dp_c_safe[1] = 1
    dp_b_safe[1] = 1
for i in range(1,n):
    ts = dp_t_safe[i]
    td = dp_t_dan[i]
    cs = dp_c_safe[i]
    cd = dp_c_dan[i]
    bs = dp_b_safe[i]
    bd = dp_b_dan[i]
    if i+1 in dic:
        if dic[i+1] == 1:
            td = 0
            dp_t_safe[i+1] = bs + bd + cs + cd
            dp_t_dan[i+1] = ts
            dp_c_safe[i+1] = 0
            dp_c_dan[i+1] = 0
            dp_b_safe[i+1] = 0
            dp_b_dan[i+1] = 0
        elif dic[i+1] == 2:
            cd = 0
            dp_c_safe[i + 1] = ts + td + bs + bd
            dp_c_dan[i + 1] = cs
            dp_b_safe[i + 1] = 0
            dp_b_dan[i + 1] = 0
            dp_t_safe[i + 1] = 0
            dp_t_dan[i + 1] = 0
        else:
            bd = 0
            dp_b_safe[i + 1] = cs + cd + ts + td
            dp_b_dan[i + 1] = bs
            dp_t_safe[i + 1] = 0
            dp_t_dan[i + 1] = 0
            dp_c_safe[i + 1] = 0
            dp_c_dan[i + 1] = 0
    else:
        dp_t_safe[i + 1] = bs + bd + cs + cd
        dp_t_dan[i + 1] = ts
        dp_c_safe[i + 1] = ts + td + bs + bd
        dp_c_dan[i + 1] = cs
        dp_b_safe[i + 1] = cs + cd + ts + td
        dp_b_dan[i + 1] = bs
print((dp_t_safe[n]+dp_t_dan[n]+dp_c_safe[n]+dp_c_dan[n]+dp_b_safe[n]+dp_b_dan[n]) % 10000)