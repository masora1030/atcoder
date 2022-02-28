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
    h,w,x,y = lr()
    a=[sr() for _ in range(h)]
    x-=1
    y-=1
    ans = 1
    for j in range(x+1,h):
        if a[j][y] == '#':
            break
        else:
            ans+=1
    for j in range(x-1,-1,-1):
        if a[j][y] == '#':
            break
        else:
            ans+=1
    for j in range(y+1,w):
        if a[x][j] == '#':
            break
        else:
            ans+=1
    for j in range(y-1,-1,-1):
        if a[x][j] == '#':
            break
        else:
            ans+=1
    print(ans)