sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    a,b=lr()
    if a>0 and b==0:
        print("Gold")
    elif a==0 and b>0:
        print("Silver")
    else:
        print("Alloy")
