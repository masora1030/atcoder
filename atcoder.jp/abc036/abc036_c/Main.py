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
a = [int(input()) for i in range(n)]
b = []
for num in a:
    b.append(num)
b.sort()
dic = {}
pre = -1
count = 0
for num in b:
    if num != pre:
        dic[num] = count
        count+=1
    pre = num
ans = []

for num in a:
    ans.append(dic[num])
for num in ans:
    print(num)