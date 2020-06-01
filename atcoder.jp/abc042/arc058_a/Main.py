inf = 10**18
mod = 10**9+7

# a^n
def power(a,n,mod):
    x = 1
    while n:
        if n & 1:
            x *= a % mod
        n >>= 1
        a *= a % mod
    return x % mod


n,k = map(int, input().split())
d = list(input().split())
ans = n
for i in range(n, n*10+1):
    tmp = str(i)
    ok = True
    for c in tmp:
        if c in d:
            ok = False
            break
    if ok:
        ans = i
        break
print(ans)