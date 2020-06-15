# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
# list(map(int, list(input()))) # スペースがない数字リストを読み込み
import math
import sys
import bisect
import heapq  # 優先度付きキュー(最小値取り出し)
import collections
from collections import deque
import pprint

inf = 10**18
mod = 10**9+7

n = int(input())
a = list(map(int, input().split()))
a.sort()
if n == 1:
    print(1)
    sys.exit()
if n == 2:
    if a[0] == a[1]:
        print(0)
    elif a[1]%a[0] == 0:
        print(1)
    else:
        print(2)
    sys.exit()

b = []
pre = a[0]
if a[0] != a[1]:
    if pre == 1:
        print(1)
        sys.exit()
else:
    if pre == 1:
        print(0)
        sys.exit()

judge = [False for i in range(10**6+1)]
for num in a:
    judge[num] = True
for i in range(1,(10**6)):
    if judge[i]:
        for j in range(i*2,10**6+1,i):
            judge[j] = False
ans = 0
for i in range(1,10**6+1):
    if judge[i]:
        ans+=1
subans = 0
c = collections.Counter(a)
for k,v in c.items():
    if v > 1 and judge[k]:
        subans+=1
print(ans-subans)