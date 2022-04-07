sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    n,k = lr()
    a=lr()
    b=lr()
    dpa=[False for _ in range(n)]
    dpb=[False for _ in range(n)]
    dpa[0]=True
    dpb[0]=True
    now_p = [a[0], b[0]]
    for i in range(1,n):
        next_p = [-1, -1]
        if (now_p[0] != -1 and now_p[0]-k <= a[i] <= now_p[0]+k) or (now_p[1] != -1 and now_p[1]-k <= a[i] <= now_p[1]+k):
            next_p[0] = a[i]
        if (now_p[0] != -1 and now_p[0]-k <= b[i] <= now_p[0]+k) or (now_p[1] != -1 and now_p[1]-k <= b[i] <= now_p[1]+k):
            next_p[1] = b[i]
        now_p = next_p
    if now_p[0] != -1 or now_p[1] != -1:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
