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
    ans=2*inf
    a=10**6
    for b in range(10**6+1):
        d=n-b*b*b
        if d<0:
            break
        while a*a*a+a*a*b+a*b*b+b*b*b >= n:
            ans=min(ans, a*a*a+a*a*b+a*b*b+b*b*b)
            a-=1
    print(ans)

if __name__ == '__main__':
    main()
