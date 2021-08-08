import sys
sys.setrecursionlimit(10**6)
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
    n=ir()
    e=[[] for i in range(n)]
    for i in range(n-1):
        a,b = lr()
        a-=1
        b-=1
        e[a].append(b)
        e[b].append(a)
    for i in range(n):
        e[i].sort()
    ans = []
    def dfs(i, root):
        ans.append(i+1)
        for num in e[i]:
            if num != root:
                dfs(num, i)
                ans.append(i+1)
    dfs(0,-1)
    print(*ans, sep=' ')