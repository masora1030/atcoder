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

x,n = map(int, input().split())
if n == 0:
    print(x)
    sys,exit()
p = list(map(int, input().split()))
p.sort()
ind = bisect.bisect_left(p,x)
if ind == n:
    print(x)
elif ind == 0:
    if p[ind] != x:
        print(x)
    else:
        print(x-1)
else:
    if p[ind] != x:
        print(x)
    else:
        maxans = 0
        minans = inf
        pre = x
        k = ind
        while k != n and pre == p[k]:
            k+=1
            pre+=1
        maxans = p[k-1]+1
        pre = x
        k = ind
        while k != -1 and pre == p[k]:
            k-=1
            pre-=1
        minans = p[k+1]-1
        ans = 0
        if abs(x-maxans) < abs(x-minans):
            ans = maxans
        else:
            ans = minans
        print(ans)