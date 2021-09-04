sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    n = ir()
    p = lr()
    q = [0 for i in range(n)]
    for i,num in enumerate(p):
        q[num-1] = i+1
    print(*q, sep=" ")