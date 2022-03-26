from collections import deque
import random
import time

sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

def main():
    start_time=time.perf_counter()
    pre_time=1.9
    a = input().split()
    sy,sx,ty,tx = map(int, a[:4])
    p = float(a[-1])
    h = [sr() for _ in range(20)]
    v = [sr() for _ in range(19)]
    pre_dir = [['' for _ in range(20)] for _ in range(20)]
    pre_dir[sy][sx] = 'S'
    q = deque([[sy, sx]])
    dirs = {'U':[-1,0], 'R':[0,1], 'D':[1,0], 'L':[0,-1]}
    while q:
        now_y, now_x = q.popleft()
        for dir_k, dir_v in dirs.items():
            ny, nx = now_y+dir_v[0], now_x+dir_v[1]
            if 0<=ny<20 and 0<=nx<20:
                if dir_k == 'U':
                    if 0<=now_y-1<19 and 0<=now_x<20 and v[now_y-1][now_x] == '0' and pre_dir[ny][nx] == '':
                        pre_dir[ny][nx] = 'U'
                        q.append([ny, nx])
                elif dir_k == 'D':
                    if 0<=now_y<19 and 0<=now_x<20 and v[now_y][now_x] == '0' and pre_dir[ny][nx] == '':
                        pre_dir[ny][nx] = 'D'
                        q.append([ny, nx])
                elif dir_k == 'R':
                    if 0<=now_y<20 and 0<=now_x<19 and h[now_y][now_x] == '0' and pre_dir[ny][nx] == '':
                        pre_dir[ny][nx] = 'R'
                        q.append([ny, nx])
                elif dir_k == 'L':
                    if 0<=now_y<20 and 0<=now_x-1<19 and h[now_y][now_x-1] == '0' and pre_dir[ny][nx] == '':
                        pre_dir[ny][nx] = 'L'
                        q.append([ny, nx])
    default_root=[]
    now_y, now_x = ty, tx
    while not (now_y == sy and now_x == sx):
        now_dir = pre_dir[now_y][now_x]
        default_root.append(now_dir)
        dy = -dirs[now_dir][0]
        dx = -dirs[now_dir][1]
        now_y+=dy
        now_x+=dx
    default_root.reverse()

    double_root = []
    for i in range(2):
        for c in default_root:
            double_root.append(c)
        double_root.append('U')
        double_root.append('R')
        double_root.append('D')
    ans_root = []
    save_root = []

    def judge_score(p, ans_root):
        scores = 0
        for i in range(100):
            root = []
            for c in ans_root:
                coin=random.random()
                if coin < 1-p:
                    root.append(c)
            now_y, now_x = sy, sx
            dist = 0
            for c in root:
                dy, dx = dirs[c]
                ny, nx = now_y+dy, now_x+dx
                if 0<=ny<20 and 0<=nx<20:
                    if c == 'U' and 0<=now_y-1<19 and 0<=now_x<20 and v[now_y-1][now_x] == '0':
                        now_y, now_x = ny, nx
                    elif c == 'D' and 0<=now_y<19 and 0<=now_x<20 and v[now_y][now_x] == '0':
                        now_y, now_x = ny, nx
                    elif c=='R' and 0<=now_y<20 and 0<=now_x<19 and h[now_y][now_x] == '0':
                        now_y, now_x = ny, nx
                    elif c=='L' and 0<=now_y<20 and 0<=now_x-1<19 and h[now_y][now_x-1] == '0':
                        now_y, now_x = ny, nx
                dist+=1
                if now_y==ty and now_x==tx:
                    scores+=1/dist
                    break
        return scores

    if len(double_root) > 200:
        save_root = ''.join(double_root[:200])
    else:
        max_score = 0
        while True:
            end_time=time.perf_counter()
            elapsed_time=end_time-start_time
            if elapsed_time>pre_time:
                break
            ans_root = double_root
            ret = 200 - len(ans_root)
            kouho = list(dirs.keys())
            for _ in range(ret):
                ans_root.append(random.choice(kouho))
            pre_score = judge_score(p, ans_root)
            if pre_score >= max_score:
                save_root = ''.join(ans_root)
                max_score = pre_score

    print(save_root)

if __name__ == '__main__':
    main()
