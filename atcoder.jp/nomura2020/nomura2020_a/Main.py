inf = 10 ** 15
mod = 10 ** 9 + 7
h1,m1,h2,m2,k = map(int, input().split())
ans = ((h2-h1)*60+(m2-m1))-k
print(ans)