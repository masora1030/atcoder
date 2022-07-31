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
    a=lr()
    total=0
    ans=0
    for i in range(n):
        if a[i] == i+1:
            total+=1
        else:
            if a[a[i]-1] == i+1:
                ans+=1
    ans//=2
    ans+=total*(total-1)//2
    print(ans)


if __name__=='__main__':
    main()
