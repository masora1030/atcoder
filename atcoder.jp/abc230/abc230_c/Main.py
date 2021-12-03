sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# mod = 10**9+7
mod = 998244353

if __name__=='__main__':
    n,a,b = lr()
    p,q,r,s = lr()
    # p-=1
    # q-=1
    # r-=1
    # s-=1
    h=q-p+1
    w=s-r+1
    ans = [['.' for j in range(w)] for i in range(h)]
    k_min = max(p-a, r-b)
    k_max = min(q-a, s-b)
    for k in range(k_min, k_max+1):
        i = k+a-p
        j = k+b-r
        ans[i][j] = '#'

    k_min = max(p-a, b-s)
    k_max = min(q-a, b-r)
    for k in range(k_min, k_max+1):
        i = k+a-p
        j = b-k-r
        ans[i][j] = '#'


    for i in range(h):
        print(*ans[i], sep="")