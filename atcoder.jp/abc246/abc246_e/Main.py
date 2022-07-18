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
    n=ir()
    sy, sx=lr()
    sx-=1
    sy-=1
    ty, tx=lr()
    tx-=1
    ty-=1
    s=[sr() for _ in range(n)]
    dist=[[inf for _ in range(n)] for _ in range(n)]
    dist[sy][sx]=0
    q=deque([[sy, sx]])
    dirs=[[1, 1], [1, -1], [-1, 1], [-1, -1]]
    while q:
        now_y, now_x=q.popleft()
        now_d=dist[now_y][now_x]
        for dir in dirs:
            ny, nx=now_y+dir[0], now_x+dir[1]
            while 0<=nx<n and 0<=ny<n and s[ny][nx]=="." and dist[ny][nx] > now_d:
                if dist[ny][nx] > now_d+1:
                    dist[ny][nx]=now_d+1
                    q.append([ny, nx])
                ny, nx=ny+dir[0], nx+dir[1]
    if dist[ty][tx]!=inf:
        print(dist[ty][tx])
    else:
        print(-1)

if __name__=='__main__':
    main()
