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
b = list(map(int, input().split()))
ans = []
while b:
    ind = -1
    for i,c in enumerate(b):
        if i+1 == c:
            ind = i
    if ind == -1:
        print(-1)
        sys.exit()
    ans.append(b.pop(ind))
ans.reverse()
for tmp in ans:
    print(tmp)