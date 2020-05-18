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
ck = ['A', 'B', 'X', 'Y']
ans = inf
for i in range(4):
    a = ck[i]
    for h in range(4):
        b = ck[h]
        for u in range(4):
            c = ck[u]
            for j in range(4):
                d = ck[j]
                count = 0
                w = 0
                while w+1 < n:
                    if (s[w] == a and s[w+1] == b) or (s[w] == c and s[w+1] == d):
                        count+=1
                        w+=2
                    else:
                        count+=1
                        w+=1
                if w == n-1:
                    count+=1
                ans = min(ans, count)
print(ans)
