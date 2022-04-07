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
    a=lr()
    c=lr()
    c.reverse()
    a.reverse()
    b = []
    if n >= m:
        for i in range(n+m+1):
            if i < m+1:
                now_a = a[0]
                ret = c[i]
                for j in range(i):
                    ret -= a[j+1]*b[len(b)-1-j]
                now_b = ret//now_a
                b.append(now_b)
            else:
                break
    else:
        for i in range(n+m+1):
            if i < n+1:
                now_a=a[0]
                ret=c[i]
                for j in range(i):
                    ret-=a[j+1]*b[len(b)-1-j]
                now_b=ret//now_a
                b.append(now_b)
            elif i < m+1:
                now_a=a[0]
                ret=c[i]
                for j in range(n):
                    ret-=a[j+1]*b[len(b)-1-j]
                now_b=ret//now_a
                b.append(now_b)
            else:
                break
    b.reverse()
    print(*b, sep=" ")


if __name__ == '__main__':
    main()
