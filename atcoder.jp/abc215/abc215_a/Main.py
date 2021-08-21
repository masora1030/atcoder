sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    s=sr()
    if s == "Hello,World!":
        print("AC")
    else:
        print("WA")