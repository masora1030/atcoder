import sys
import bisect
from collections import deque

# sys.setrecursionlimit(10**4)
# from sys import stdin
# readline = stdin.readline
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
mod=10**9+7
# mod = 998244353

if __name__=='__main__':
    n=ir()
    e = [[] for i in range(n)]
    for m in range(n-1):
        a,b = lr()
        a-=1
        b-=1
        e[a].append(b)
        e[b].append(a)
    ans = []
    q = deque([[0,0]])
    visited = [False for i in range(n)]
    visited[0] = True
    ans.append(0)
    while q:
        now, depth = q.popleft()
        for ne in e[now]:
            if not visited[ne]:
                if (depth+1)%2 == 0:
                    ans.append(ne)
                q.append([ne, depth+1])
                visited[ne] = True
    if len(ans) >= n//2:
        ans_1 = []
        for i in range(n//2):
            ans_1.append(ans[i]+1)
        print(*ans_1, sep=" ")
    else:
        ans_1 = [True for i in range(n)]
        for num in ans:
            ans_1[num] = False
        ind = 0
        ans_2 = []
        for i in range(n):
            if ind < n//2:
                if ans_1[i]:
                    ans_2.append(i+1)
                    ind+=1
            else:
                break
        print(*ans_2, sep=" ")