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
    if n%4==2:
        print(n)
    elif n%4==1:
        print(n+1)
    elif n%4==0:
        print(n+2)
    else:
        print(n+3)



if __name__=='__main__':
    main()
