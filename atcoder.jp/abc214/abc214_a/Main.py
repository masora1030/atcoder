sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    n=ir()
    if 1<= n <126:
        print(4)
    elif 126<=n < 212:
        print(6)
    else:
        print(8)