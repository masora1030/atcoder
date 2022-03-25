sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

import sys

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    n=ir()
    xy = [lr() for _ in range(n)]
    s=sr()
    Rdiclist = {}
    Ldiclist = {}
    for i in range(n):
        x,y = xy[i]
        c = s[i]
        if c == 'R':
            if y in Rdiclist:
                Rdiclist[y] = min(x, Rdiclist[y])
            else:
                Rdiclist[y] = x
        else:
            if y in Ldiclist:
                Ldiclist[y] = max(x, Ldiclist[y])
            else:
                Ldiclist[y] = x
    flg = False
    for k in Rdiclist:
        if k in Ldiclist:
            if Ldiclist[k] > Rdiclist[k]:
                flg = True
                break
    if flg:
        print("Yes")
    else:
        print("No")



if __name__ == '__main__':
    main()
