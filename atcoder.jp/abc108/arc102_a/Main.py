inf = 10 ** 15
mod = 10 ** 9 + 7
n,k = map(int, input().split())
tmp = n//k
ans = (tmp*tmp*tmp)
if k % 2 == 1:
    print(ans)
if k % 2 == 0:
    tmp = (2*n+k)//(2*k)
    ans += (tmp*tmp*tmp)
    print(ans)