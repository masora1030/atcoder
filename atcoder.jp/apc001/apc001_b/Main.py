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
a = list(map(int, input().split()))
b = list(map(int, input().split()))
suma = sum(a)
sumb = sum(b)
count = sumb-suma
suba = 0
subb = 0
if count < 0:
    print('No')
    sys.exit()
for i in range(n):
    if a[i] > b[i]:
        suba+=abs(a[i]-b[i])
    else:
        subb+=(abs(a[i]-b[i])+1)//2
if max(suba, subb) <= count:
    print('Yes')
else:
    print('No')