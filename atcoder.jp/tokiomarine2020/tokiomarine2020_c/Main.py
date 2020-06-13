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

n,k = map(int, input().split())
b = list(map(int, input().split()))
a = [0]
for i in b:
    a.append(i)

flag = False
while k > 0 and (not flag):
    flag = True
    a2 = [0 for i in range(n+1)]
    for i,num in enumerate(a[1:]):
        l = max(i-num,0)
        r = min(i+num,n-1)
        l+=1
        r+=1
        a2[l] += 1
        if r+1 != n+1:
            a2[r+1] -= 1

    a = [0 for i in range(n+1)]
    for i in range(1, n+1):
        a[i] += a[i-1] + a2[i]
        if a[i] != n:
            flag=False
    k-=1
if flag:
    print(*[n for i in range(n)], sep=' ')
else:
    print(*a[1:], sep=' ')