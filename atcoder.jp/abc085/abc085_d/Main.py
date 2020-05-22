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

n,h = map(int, input().split())
blist = []
amax = 0
for i in range(n):
    a,b = map(int, input().split())
    amax = max(amax, a)
    blist.append(b)
# aが最大のやつじゃないとフル価値なし
ans = (h+amax-1)//amax
blist.sort(reverse = True)
btotal=0
for i,num in enumerate(blist):
    tmp = h
    if num <= amax:
        break
    else:
        btotal+=num
        tmp-=btotal
        if tmp <= 0:
            ans = min(ans, i+1)
            break
        else:
            ans = min((tmp+amax-1)//amax + i+1, ans)
print(ans)



