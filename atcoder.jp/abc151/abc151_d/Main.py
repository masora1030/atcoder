from collections import deque
def bfs(h,w,m,sy,sx):
    INF = 10**12
    max_length = 0
    # すべての点を INF で初期化
    d = [[INF for j in range(w)] for i in range(h)]
    
    # 移動4方向のベクトル
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    # スタート地点をキューに入れ、その点の距離を0にする
    q = deque([])
    q.append((sx,sy))
    d[sy][sx] = 0
    
    # キューが空になるまでループ
    while q:
        #キューの先頭を取り出す
        p = q.popleft()
        #四方向移動
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]
            if 0 <= nx and nx < w and 0 <= ny and ny < h and m[ny][nx] != '#' and d[ny][nx] == INF:
                q.append((nx,ny))
                d[ny][nx] = d[p[1]][p[0]] + 1
                if d[ny][nx] > max_length:
                    max_length = d[ny][nx]
    return max_length

h,w = map(int, input().split())
m = []
max_len = 0
for i in range(h):
    m.append(input())
for i in range(h):
    for j in range(w):
        if m[i][j] == '.':
            length = bfs(h,w,m,i,j)
            if length > max_len:
                max_len = length
print(max_len)