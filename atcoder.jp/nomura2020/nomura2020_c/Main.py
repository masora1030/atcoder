# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
import math
import sys
import bisect
import heapq  # 優先度付きキュー(最小値取り出し)
from collections import deque
inf = 10 ** 15
mod = 10 ** 9 + 7
n = int(input())
a = list(map(int, input().split()))
preoya = 1
arieruoya = [0 for i in range(n+1)]
for i in range(n):
    arieruoya[i] = preoya
    l = a[i]
    if l > preoya*2-1:
        print(-1)
        sys.exit()
    preoya = min((preoya-l)*2,10**13)
if a[n] > preoya:
    print(-1)
    sys.exit()
arieruoya[n] = 0

a.reverse()
premax = a[0]
premin = (a[0]+1)//2
ans=premax
for i in range(1,n+1):
    l = a[i]
    premax = min(arieruoya[n-i], premax+l)
    ans+=premax
print(ans)