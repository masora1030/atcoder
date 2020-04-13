n = int(input())
a = list(map(int, input().split()))

import fractions
tmp = a[0]
for num in a:
    tmp = fractions.gcd(tmp, num)           #最大公約数
print(tmp)