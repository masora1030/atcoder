inf=10**18
# mod = 10**9+7
mod=998244353

# segment tree

def main():
    h,w,c = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(h)]
    apc = [[inf]*(w+1) for _ in range(h+1)]
    amc = [[inf]*(w+1) for _ in range(h+1)]
    ans = inf
    for i in range(h):
        for j in range(w):
            amc[i+1][j+1] = min(amc[i][j+1], amc[i+1][j], a[i][j]-c*(i+j))
            tmp = a[i][j]+c*(i+j)
            ans = min(ans, tmp+amc[i][j+1], tmp+amc[i+1][j])
    for i in range(h):
        for j in range(w-1, -1, -1):
            apc[i+1][j] = min(apc[i][j], apc[i+1][j+1], a[i][j]-c*(i-j))
            tmp = a[i][j]+c*(i-j)
            ans = min(ans, tmp+apc[i][j], tmp+apc[i+1][j+1])
    print(ans)

if __name__ == '__main__':
    main()
