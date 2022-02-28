sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

import sys

inf=10**18
# mod = 10**9+7
mod=998244353
import math

if __name__=='__main__':
    n=ir()
    x0, y0 = lr()
    xn2, yn2 = lr()
    r = math.sqrt((x0-xn2)**2 + (y0-yn2)**2)/2
    x_origin = (x0+xn2)/2
    y_origin = (y0+yn2)/2
    x_sub = x0-x_origin
    y_sub = y0-y_origin

    tmp = n//2
    p = 180
    arg = p/tmp
    c=math.cos(math.radians(arg))
    s=math.sin(math.radians(arg))
    ans_x, ans_y = x_origin+x_sub*c-y_sub*s, y_origin+x_sub*s+y_sub*c
    print(ans_x, ans_y)
