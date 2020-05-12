import fractions
import sys
import bisect
import heapq  # 優先度付きキュー(最小値取り出し)

inf = 10 ** 15
mod = 10 ** 9 + 7
n,x = map(int, input().split())
a = list(map(int, input().split()))
ans = abs(a[0]-x)
for i in range(n):
    ans = fractions.gcd(ans, abs(a[i]-x))
print(ans)