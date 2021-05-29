import sys

# sys.setrecursionlimit(10**4)
# from sys import stdin
# readline = stdin.readline
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    n=ir()
    xy = [lr() for i in range(n)]
    for i in range(n):
        xy[i].append(i)
    xy.sort(key=lambda x:x[0])
    kouho = []
    inds = []
    kouho.append(max(abs(xy[-1][0] - xy[0][0]), abs(xy[-1][1] - xy[0][1])))
    inds.append([xy[-1][2], xy[0][2]])
    kouho.append(max(abs(xy[-2][0]-xy[0][0]), abs(xy[-2][1]-xy[0][1])))
    inds.append([xy[-2][2], xy[0][2]])
    kouho.append(max(abs(xy[-1][0]-xy[1][0]), abs(xy[-1][1]-xy[1][1])))
    inds.append([xy[-1][2], xy[1][2]])
    for i in range(3):
        inds[i][0], inds[i][1] = min(inds[i][0], inds[i][1]), max(inds[i][0], inds[i][1])

    xy.sort(key=lambda x:x[1])

    x,y = min(xy[-1][2], xy[0][2]), max(xy[-1][2], xy[0][2])
    flg = True
    for xx,yy in inds:
        if x==xx and y==yy:
            flg=False
    if flg:
        kouho.append(max(abs(xy[-1][0]-xy[0][0]), abs(xy[-1][1]-xy[0][1])))
    x, y=min(xy[-2][2], xy[0][2]), max(xy[-2][2], xy[0][2])
    flg=True
    for xx, yy in inds:
        if x==xx and y==yy:
            flg=False
    if flg:
        kouho.append(max(abs(xy[-2][0]-xy[0][0]), abs(xy[-2][1]-xy[0][1])))
    x, y=min(xy[-1][2], xy[1][2]), max(xy[-1][2], xy[1][2])
    flg=True
    for xx, yy in inds:
        if x==xx and y==yy:
            flg=False
    if flg:
        kouho.append(max(abs(xy[-1][0]-xy[1][0]), abs(xy[-1][1]-xy[1][1])))
    kouho.sort()
    print(kouho[-2])