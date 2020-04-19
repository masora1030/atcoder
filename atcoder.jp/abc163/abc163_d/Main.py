mod = 10**9+7

n,k = map(int, input().split())
count = 0
for i in range(n+1-k+1):
    j = k+i
    count += (((2*n-(j-1))*(j)//2 - (j-1)*(j)//2) + 1)
    count = count % mod
print(count)