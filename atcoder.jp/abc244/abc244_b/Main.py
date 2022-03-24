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
    s=sr()
    sx,sy = 0,0
    dir_dic = {0:[1,0], 1:[0,-1], 2:[-1,0], 3:[0,1]}
    now_dir = 0
    for c in s:
        if c == 'S':
            dx,dy = dir_dic[now_dir%4]
            sx+=dx
            sy+=dy
        else:
            now_dir+=1
    print(sx,sy)
