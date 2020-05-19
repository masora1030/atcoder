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
s = input()
stack = []
ans = deque(list(s))
countl = 0
countr = 0
for c in s:
    if c == '(':
        stack.append('(')
    if c == ')':
        if stack:
            stack.pop()
        else:
            countl+=1
countr = len(stack)
for i in range(countl):
    ans.appendleft('(')
for i in range(countr):
    ans.append(')')
print(''.join(ans))