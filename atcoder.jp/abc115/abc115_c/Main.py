inf = 10**9+7
mod = 10**9+7
n,k = map(int, input().split())
a = [int(input()) for i in range(n)]
a.sort()
minh = inf
for i in range(n-k+1):
    minh = min(minh, a[i+k-1]-a[i])
print(minh)