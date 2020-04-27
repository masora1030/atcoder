inf = 10**15
mod = 10**9+7
k,s = map(int, input().split())
ans = 0
for i in range(k+1):
    tmp = s-i
    if tmp >= 0:
        for j in range(k+1):
            t = tmp-j
            if 0 <= t <= k:
                ans += 1
print(ans)