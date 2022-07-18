sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    n,k,x=lr()
    a=lr()
    a.sort(reverse=True)
    # 0 ijou
    for i in range(n):
        now = a[i]
        tmp = now//x
        if k >= tmp:
            k-=tmp
            a[i]=now-tmp*x
        else:
            a[i]=now-k*x
            k=0
            break
    a.sort(reverse=True)
    for i in range(n):
        if k==0:
            break
        a[i]=0
        k-=1
    print(sum(a))

if __name__ == '__main__':
    main()
