sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    n,x = lr()
    a = lr()
    ans = 1
    visited = [False for i in range(n)]
    visited[x-1]=True
    ne = a[x-1]-1
    while not visited[ne]:
        visited[ne]=True
        ne=a[ne]-1
        ans+=1
    print(ans)

