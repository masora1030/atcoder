import bisect

sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

import sys

inf=10**18
# mod = 10**9+7
mod=998244353

if __name__=='__main__':
    n=ir()
    p=lr()
    depth2ins = [[] for _ in range(n)]
    in_outs = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    e = [[] for _ in range(n)]
    for chi,par in enumerate(p):
        par-=1
        e[par].append(chi+1)

    now_time = 0
    stack = [[0,0]]
    while stack:
        now_r, now_depth = stack[-1]
        if visited[now_r]:
            stack.pop()
            in_outs[now_r].append(now_time)
            now_time+=1
            continue
        visited[now_r] = True
        in_outs[now_r].append(now_time)
        depth2ins[now_depth].append(now_time)
        now_time+=1
        for chi in e[now_r]:
            stack.append([chi, now_depth+1])
    q=ir()
    for _ in range(q):
        u,d = lr()
        in_time, out_time = in_outs[u-1]
        if depth2ins[d]:
            in_ind = bisect.bisect_left(depth2ins[d], in_time)
            out_ind = bisect.bisect_left(depth2ins[d], out_time)
            print(out_ind-in_ind)
        else:
            print(0)
