sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    s,t,x = lr()
    if s > t:
        if s <= x <= 23 or 0 <= x < t:
            print("Yes")
        else:
            print("No")
    else:
        if s <= x < t:
            print("Yes")
        else:
            print("No")