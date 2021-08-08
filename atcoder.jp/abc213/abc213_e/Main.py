from collections import deque
import itertools
import math
import heapq
import random

# import sys
# sys.setrecursionlimit(10**6)
from sys import stdin
# readline = stdin.readline
# sr=lambda: readline()
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    h,w = lr()
    s = [sr() for i in range(h)]
    q = deque([[0, 0, 0]])
    ma = [[max(h,w) for j in range(w)] for i in range(h)]
    ma[0][0] = 0
    normal = [[0,1], [0,-1], [1,0], [-1,0]]
    sugoi = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            if not ((i==-2 and j==-2) or (i==-2 and j==2) or (i==2 and j==-2) or (i==2 and j==2) or (i==0 and j==0)):
                sugoi.append([i, j])
    while q:
        y,x,c = q.popleft()
        for dy,dx in normal:
            ny,nx = y+dy, x+dx
            if 0<=ny<h and 0<=nx<w:
                if s[ny][nx] == '.' and ma[ny][nx] > c:
                    q.appendleft([ny, nx, c])
                    ma[ny][nx] = c
        for dy,dx in sugoi:
            ny,nx = y+dy, x+dx
            if 0<=ny<h and 0<=nx<w:
                if ma[ny][nx] > c+1:
                    q.append([ny, nx, c+1])
                    ma[ny][nx] = c+1
    print(ma[h-1][w-1])