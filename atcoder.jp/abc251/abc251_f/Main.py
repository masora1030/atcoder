from collections import deque
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353


def main():
    n,m=lr()
    # T1:深さ優先
    # T2:幅優先
    e1=[[] for _ in range(n)]
    e2=[[] for _ in range(n)]
    for _ in range(m):
        u,v=lr()
        u-=1
        v-=1
        e1[u].append(v)
        e1[v].append(u)
        e2[v].append(u)
        e2[u].append(v)

    ans=[]
    # T1
    checkpoints = set()
    q = [0]
    checkpoints.add(0)
    while q:
        now = q[-1]
        # print(q)
        if e1[now]:
            next = e1[now].pop()
            if not next in checkpoints:
                q.append(next)
                checkpoints.add(next)
                ans.append([now+1, next+1])
        else:
            q.pop()
    # print(ans)

    # T2
    visited = set()
    q = deque([0])
    visited.add(0)
    while q:
        now = q.popleft()
        for next in e2[now]:
            if not next in visited:
                q.append(next)
                visited.add(next)
                ans.append([now+1, next+1])

    for v,u in ans:
        print(v,u)

if __name__=='__main__':
    main()
