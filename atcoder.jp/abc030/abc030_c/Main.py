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

n,m = map(int, input().split())
x,y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
now = 0
while 1:
    aind = bisect.bisect_left(a, now)
    if aind == n:
        break
    now = a[aind] + x
    bind = bisect.bisect_left(b, now)
    if bind == m:
        break
    now = b[bind] + y
    ans+=1
print(ans)