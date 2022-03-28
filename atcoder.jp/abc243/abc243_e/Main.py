sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    n,m = lr()
    es = []
    d=[[inf]*n for _ in range(n)]
    for i in range(m):
        a,b,c = lr()
        es.append([a-1,b-1,c])
        d[a-1][b-1] = c
        d[b-1][a-1] = c
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    ans=0
    for a,b,c in es:
        for k in range(n):
            if d[a][k] + d[k][b] <= c:
                ans+=1
                break
    print(ans)

if __name__ == '__main__':
    main()
