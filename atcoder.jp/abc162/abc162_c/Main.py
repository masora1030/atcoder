from math import gcd
k = int(input())
ans = 0
for i in range(1,k+1):
    for j in range(1,k+1):
        for l in range(1,k+1):
            f = gcd(i, j)
            ans += gcd(f, l)
print(ans)