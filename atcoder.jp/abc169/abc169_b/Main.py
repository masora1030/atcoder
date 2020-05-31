# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
import math
import sys
import bisect
import heapq  # 優先度付きキュー(最小値取り出し)
from collections import deque
inf = 10 ** 18
mod = 10 ** 9 + 7
n = int(input())
a = list(map(int, input().split()))
tmp = 1
for i in a:
    if i == 0:
        print(0)
        sys.exit()
for i in a:
    if i > inf:
        print(-1)
        sys.exit()
    tmp = tmp*i
    if tmp > inf:
        print(-1)
        sys.exit()
print(tmp)