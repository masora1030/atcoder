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
xy = [list(map(int, input().split())) for i in range(n)]
xsub = 0
dicx = {}
xy.sort(reverse=True)
for i in range(n-1):
    for j in range(i+1,n):
        prex,prey = xy[i]
        x, y = xy[j]
        tmpx = x - prex
        tmpy = y - prey
        if (tmpx, tmpy) in dicx:
            dicx[(tmpx, tmpy)] += 1
        else:
            dicx[(tmpx, tmpy)] = 1
for _,num in dicx.items():
    xsub = max(num, xsub)
print(n-xsub)




