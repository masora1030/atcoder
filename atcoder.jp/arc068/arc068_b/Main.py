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

inf = 10**18
mod = 10**9+7

n = int(input())
a = list(map(int, input().split()))
c = collections.Counter(a)
kind = 0
for k,v in c.items():
    if v%2==0:
        kind+=1
if kind%2==0:
    print(len(c))
else:
    print(len(c)-1)