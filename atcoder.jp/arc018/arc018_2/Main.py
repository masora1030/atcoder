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
xy = [list(map(int, input().split())) for i in range(n)]
ans = 0
for i in range(n-2):
    x1,y1 = xy[i]
    for j in range(i+1,n-1):
        x2,y2 = xy[j]
        vec = [abs(x1 - x2), abs(y1 - y2)]
        for k in range(j+1,n):
            x3,y3 = xy[k]
            if vec[0] != 0 and vec[1] != 0:
                vec2 = [abs(x1 - x3), abs(y1 - y3)]
                if vec2[1]*vec[0] == vec2[0]*vec[1]:
                    continue
            elif vec[0] == 0 and x3 == x1:
                continue
            elif vec[1] == 0 and y3 == y1:
                continue
            men = (abs(x1-x2)*abs(y1-y2) + abs(x2-x3)*abs(y2-y3) + abs(x3-x1)*abs(y3-y1))
            if men%2 == 0:
                ans+=1
print(ans)
print('')