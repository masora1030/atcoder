# Union Find
class UnionFind():
    def __init__(self, n):
        self.n=n
        self.parents=[-1]*n

    def find(self, x):
        if self.parents[x]<0:
            return x
        else:
            self.parents[x]=self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x=self.find(x)
        y=self.find(y)

        if x==y:
            return

        if self.parents[x]>self.parents[y]:
            x, y=y, x

        self.parents[x]+=self.parents[y]
        self.parents[y]=x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x)==self.find(y)

    def members(self, x):
        root=self.find(x)
        return [i for i in range(self.n) if self.find(i)==root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x<0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

    def all_family_count(self):
        return [-min(0, x) for i, x in enumerate(self.parents)]

    def memberlist(self):
        self.L=[set() for _ in range(self.n)]
        for i in range(self.n):
            if self.parents[i]<0:
                self.L[i].add(i)
            else:
                self.L[self.find(i)].add(i)
        return self.L


import sys
import bisect
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

import random
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    N,K,B= lr()
    maps = [[0 for i in range(N)] for j in range(N)] # num of b at a cell
    one_block_map = [[False for i in range(N)] for j in range(N)]
    signed_map = [[False for i in range(N)] for j in range(N)]
    signed_list = []
    blocks = []
    init_y, init_x = -1, -1
    now_score = inf

    # input
    for i in range(K):
        y,x = lr()
        if init_y == -1:
            init_y, init_x = y,x
        signed_map[y][x] = True
        signed_list.append([y,x])
    b_data = []
    for i in range(B):
        n,m,c = lr()
        b_maps = [sr() for j in range(n)]
        data = [n,m,c,b_maps]
        b_data.append(data)
    b_data.sort(key=lambda x:x[2])


    def connect_judge():
        q = deque([[init_y, init_x]])
        visited = [[False for i in range(N)] for j in range(N)]
        visited[init_y][init_x] = True
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while q:
            now_y, now_x = q.popleft()
            for dy, dx in dirs:
                ny, nx = now_y+dy, now_x+dx
                if 0<=ny<N and 0<=nx<N and visited[ny][nx] == False and maps[ny][nx] == 1:
                    visited[ny][nx] = True
                    q.append([ny, nx])
        flg = True
        for i in range(N):
            for j in range(N):
                if signed_map[i][j] and visited[i][j] == False:
                    flg = False
                    break
            if not flg:
                break
        return flg

    # simple ans 2 (minimum zeniki ki) (initial ans)
    def init_ans():
        e = []
        for i in range(K-1):
            i_y, i_x = signed_list[i][0], signed_list[i][1]
            for j in range(i+1,K):
                j_y, j_x = signed_list[j][0], signed_list[j][1]
                dist = abs(i_y-j_y) + abs(i_x-j_x) - 1
                e.append([i,j,dist])
        e.sort(key=lambda x:x[2])
        ret_e = []
        uf = UnionFind(K)
        for i,j,dist in e:
            if not uf.same(i,j):
                uf.union(i,j)
                ret_e.append([i,j])

        for i,j in signed_list:
            maps[i][j] = 1

        for i,j in ret_e:
            i_y, i_x = signed_list[i][0], signed_list[i][1]
            j_y, j_x = signed_list[j][0], signed_list[j][1]

            if i_y > j_y:
                tmp = j_y
                j_y = i_y
                i_y = tmp
                tmp=j_x
                j_x=i_x
                i_x=tmp

            if i_x <= j_x:
                y_min, y_max = min(i_y, j_y), max(i_y, j_y)
                x_min, x_max = min(i_x, j_x), max(i_x, j_x)
                for i in range(y_min+1, y_max):
                    maps[i][x_min]+=1
                for j in range(x_min+1, x_max):
                    maps[y_max][j]+=1
                maps[y_max][x_min]+=1
            else:
                y_min, y_max=min(i_y, j_y), max(i_y, j_y)
                x_min, x_max=min(i_x, j_x), max(i_x, j_x)
                for i in range(y_min+1, y_max):
                    maps[i][x_max]+=1
                for j in range(x_min+1, x_max):
                    maps[y_max][j]+=1
                maps[y_max][x_max]+=1

        total_cost = 0
        for i in range(N):
            for j in range(N):
                if maps[i][j] >= 2:
                    total_cost-=(maps[i][j]-1)
                    maps[i][j] = 1
                if maps[i][j] == 1:
                    total_cost+=1
                    one_block_map[i][j] = True

        return total_cost*b_data[0][2]


    # simple ans 2
    ans = []

    init_cost = init_ans()
    # for i in range(N):
    #     print(*maps[i], sep='')
    assert connect_judge() == True
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 1:
                ans.append([1,j,i])
    ans_m = len(ans)

    print(ans_m)
    for b, y, x in ans:
        print(b, x, y)

    # # simple ans 1
    # ans_m = N*N
    # ans = []
    # for m in range(ans_m):
    #     ans.append([1, m//N, m%N])
    #     maps[m//N][m%N] = 1
    #
    # assert connect_judge() == True
    # print(ans_m)
    # for b, y, x in ans:
    #     print(b, x, y)
