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
ss = []
for c in s:
    if c != 'x':
        ss.append(c)
leng = len(ss)
flag = True
for i in range(leng//2):
    if ss[i] != ss[leng-1-i]:
        flag = False
        break
if flag:
    count=0
    l = 0
    r = n-1
    while l < r:
        if s[r] != s[l]:
            if s[l] == 'x':
                count+=1
                l+=1
            else:
                count+=1
                r-=1
        else:
            r -= 1
            l += 1
    print(count)


else:
    print(-1)
