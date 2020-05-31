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
s = input()
n = len(s)
stack = []
for c in s:
    if c == 'S':
        stack.append(c)
    if c == 'T':
        if stack:
            if stack.pop() == 'T':
                stack.append('T')
                stack.append(c)
        else:
            stack.append(c)
print(len(stack))