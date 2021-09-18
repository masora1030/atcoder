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
    edge = [[] for i in range(n)]
    for _ in range(n-1):
        a,b = lr()
        a-=1
        b-=1
        edge[a].append(b)
        edge[b].append(a)
    visited = [False for i in range(n)]
    def get_ans(root):
        ret = 0
        ans = 0
        visited[root] = True
        if len(edge[root]) == 0:
            return 1, n-1
        for num in edge[root]:
            if not visited[num]:
                ret_c, ans_c = get_ans(num)
                ans+=ans_c
                ans+=ret_c*(n-ret_c)
                ret+=ret_c
        return ret+1, ans
    _, ans = get_ans(0)
    print(ans)
