sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    a,b,k=lr()
    ans=0
    while a < b:
        a*=k
        ans+=1
    print(ans)


if __name__ == '__main__':
    main()