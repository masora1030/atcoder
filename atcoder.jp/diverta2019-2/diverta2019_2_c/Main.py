# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
# list(map(int, list(input()))) # スペースがない数字リストを読み込み
import math
import sys
import bisect
import heapq  # 優先度付きキュー(最小値取り出し)
from collections import deque
inf = 10**18
mod = 10**9+7

n = int(input())
a = list(map(int, input().split()))
a.sort()
minnum = a[0]
maxnum = a[-1]
zind = bisect.bisect_left(a, 0)
ans = []
ansnum = maxnum
if zind == n:
    zind-=1
for i in range(1,zind):
    tmp = a[i]
    ans.append([maxnum, tmp])
    ansnum-=tmp
    maxnum-=tmp
ansnum -= minnum
if zind == 0:
    zind+=1
for i in range(zind, n-1):
    tmp = a[i]
    ans.append([minnum, tmp])
    ansnum+=tmp
    minnum-=tmp
ans.append([maxnum, minnum])
print(ansnum)
for p in ans:
    print(*p, sep = ' ')