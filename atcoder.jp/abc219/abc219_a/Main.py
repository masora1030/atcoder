sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
mod=10**9+7
# mod = 998244353

if __name__=='__main__':
    n=ir()
    if 0 <= n < 40:
        print(40-n)
    elif 40 <= n < 70:
        print(70-n)
    elif 70 <= n < 90:
        print(90-n)
    else:
        print("expert")