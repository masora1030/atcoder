import bisect

sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# mod = 10**9+7
mod = 998244353

if __name__=='__main__':
    n,q = lr()
    a = lr()
    a.sort()
    for _ in range(q):
        x = ir()
        ind = bisect.bisect_left(a,x)
        print(n-ind)
