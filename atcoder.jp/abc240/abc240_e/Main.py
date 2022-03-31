sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

import sys
sys.setrecursionlimit(10**9)

inf=10**18
# mod = 10**9+7
mod=998244353

num_l = 0

def main():
    global num_l
    n=ir()
    e=[[] for _ in range(n)]
    for _ in range(n-1):
        u,v=lr()
        u-=1
        v-=1
        e[u].append(v)
        e[v].append(u)
    visited=[False for _ in range(n)]
    visited[0] = True
    ans = [[] for _ in range(n)]
    def dfs(root):
        global num_l
        is_l = True
        min_l = inf
        max_l = -1
        for chi in e[root]:
            if not visited[chi]:
                is_l = False
                visited[chi]=True
                tmp_min_l, tmp_max_l = dfs(chi)
                min_l = min(tmp_min_l, min_l)
                max_l = max(tmp_max_l, max_l)
        if is_l:
            num_l+=1
            min_l=num_l
            max_l=num_l
        ans[root] = [min_l, max_l]
        return min_l, max_l
    dfs(0)
    for k,v in ans:
        print(k,v)

if __name__ == '__main__':
    main()
