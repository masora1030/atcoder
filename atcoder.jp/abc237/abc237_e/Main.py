from collections import deque
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

import sys

inf = 10**18
# mod = 10**9+7
mod = 998244353

if __name__=='__main__':
    n,m = lr()
    h = lr()
    e = [[] for _ in range(n)]
    for _ in range(m):
        a,b = lr()
        a-=1
        b-=1
        e[a].append(b)
        e[b].append(a)
    # 幅優先
    q = deque([[0,0]]) # 位置と楽しさ
    dp_max = [-inf for i in range(n)]
    dp_max[0] = 0
    ans = 0
    while q:
        now, t = q.popleft()
        now_h = h[now]
        for ne in e[now]:
            ne_h = h[ne]
            if now_h > ne_h:
                ne_t = t+(now_h-ne_h)
            else:
                ne_t = t-2*(ne_h-now_h)
            if ne_t > dp_max[ne]:
                dp_max[ne] = ne_t
                q.append([ne,ne_t])
                ans = max(ans, ne_t)
    print(ans)
