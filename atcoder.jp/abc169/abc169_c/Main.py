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
a,b = input().split()
bpre = []
for c in b:
    if c != '.':
        bpre.append(c)
a100 = int(a)
b100 = int(''.join(bpre))
ans = str(a100*b100)
if len(ans) > 2:
    print(ans[:-2])
else:
    print(0)
