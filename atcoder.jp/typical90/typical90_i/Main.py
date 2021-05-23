import sys
import bisect
import cmath

# sys.setrecursionlimit(10**4)
# from sys import stdin
# readline = stdin.readline
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
mod=10**9+7
# mod = 998244353

if __name__=='__main__':
    n=ir()
    xy = [lr() for i in range(n)]
    ans = 0
    for i in range(n):
        zx, zy = xy[i]
        arg = []
        for j in range(n):
            if j==i:
                continue
            x,y = xy[j]
            tmp = cmath.phase(complex(x-zx, y-zy))/cmath.pi*180
            arg.append(tmp)
            arg.append(tmp+360)
        arg.sort()
        for j in range(n-1):
            tmp = arg[j]+180
            ind = bisect.bisect_left(arg, tmp)
            ind2 = max(0, ind-1)
            pre = min(arg[ind]-arg[j], 360-(arg[ind]-arg[j]))
            pre2 = min(arg[ind2]-arg[j], 360-(arg[ind2]-arg[j]))
            if abs(180-pre) > abs(180-pre2):
                pre = pre2
            ans = max(ans, pre)
    print(ans)