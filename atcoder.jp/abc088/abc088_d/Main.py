# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
import sys
from collections import deque
inf = 10**15
mod = 10**9+7
R, C = map(int, input().split())
maps = [input() for i in range(R)]
whole = R*C
defoB = 0
for s in maps:
    for c in s:
        if c == '#':
            defoB+=1
dis = [[-1 for j in range(C)] for i in range(R)]

def bfsC(init_y, init_x, goal_y, goal_x):
    q = deque([[init_y, init_x]])
    dis[init_y][init_x] = 0
    while q:
        y, x = q.popleft()
        if y == goal_y and x == goal_x:
            return dis[y][x]
        distance = dis[y][x]+1
        for dy, dx in [[1,0],[-1,0],[0,1],[0,-1]]:
            if 0 <= y+dy < R and 0 <= x+dx < C and maps[y+dy][x+dx] != '#' and dis[y+dy][x+dx] == -1:
                q.append([y+dy, x+dx])
                dis[y+dy][x+dx] = distance
    return -1 # (見つからなかった)

result = bfsC(0, 0, R-1, C-1) + 1
if result != 0:
    print(whole - result - defoB)
else:
    print(-1)
