inf = 10**9+7
mod = 10**9+7
s = input()
slen = len(s)
ans = inf
for i in range(slen-2):
    a = s[i]
    b = s[i+1]
    c = s[i+2]
    tmp = int(''.join([a, b, c]))
    ans = min(ans, abs(tmp - 753))
print(ans)