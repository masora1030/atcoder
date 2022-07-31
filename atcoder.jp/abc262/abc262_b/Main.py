sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353


def main():
    n,m=lr()
    e=[set() for _ in range(n)]
    for _ in range(m):
        u,v=lr()
        u-=1
        v-=1
        e[u].add(v)
        e[v].add(u)
    ans = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if i in e[j] and j in e[k] and k in e[i]:
                    ans+=1
    print(ans)


if __name__=='__main__':
    main()
