# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
import sys
inf = 10**9+7
mod = 10**9+7

n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]

maxans = 0
for i in range(m-1):
    for j in range(i+1, m):
        count = 0
        for k in range(n):
            count += max(a[k][i], a[k][j])
        maxans = max(maxans, count)
print(maxans)
