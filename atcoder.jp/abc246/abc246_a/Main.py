sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    x1,y1 = lr()
    x2, y2=lr()
    x3, y3=lr()
    if x1==x2:
        if y1==y3:
            print(x3, y2)
        else:
            print(x3, y1)
    elif x1==x3:
        if y1==y2:
            print(x2, y3)
        else:
            print(x2, y1)
    else:
        if y2==y1:
            print(x1,y3)
        else:
            print(x1,y2)


if __name__ == '__main__':
    main()
