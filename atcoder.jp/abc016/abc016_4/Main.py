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
ax, ay, bx, by = map(int, input().split())
n = int(input())
xy = [list(map(int, input().split())) for i in range(n)]
count = 0
if bx-ax != 0:
    A = (by-ay)/(bx-ax)
    for i in range(-1,n-1):
        cx,cy = xy[i]
        dx,dy = xy[i+1]
        if dx-cx != 0:
            C = (dy-cy)/(dx-cx)
            if A != C:
                colx = (A*ax-ay-C*cx+cy)/(A-C)
                if cx <= colx <= dx or cx >= colx >= dx:
                    if ax <= colx <= bx or ax >= colx >= bx:
                        count+=1
        else:
            coly = A*(cx-ax)+ay
            if cy <= coly <= dy or cy >= coly >= dy:
                if ay <= coly <= by or ay >= coly >= by:
                    count+=1
else:
    for i in range(-1,n-1):
        cx, cy = xy[i]
        dx, dy = xy[i + 1]
        if dx - cx != 0:
            C = (dy-cy) / (dx-cx)
            coly = C*(ax-cx)+cy
            if cy <= coly <= dy or cy >= coly >= dy:
                if ay <= coly <= by or ay >= coly >= by:
                    count += 1
print(count//2+1)