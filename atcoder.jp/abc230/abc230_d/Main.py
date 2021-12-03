sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# mod = 10**9+7
mod = 998244353

if __name__=='__main__':
    n,d = lr()
    LR = [lr() for _ in range(n)]
    LR.sort(key=lambda x:x[1])
    ans = 0
    now = 0
    for l,r in LR:
        if now >= l:
            continue
        else:
            ans+=1
            now = r+d-1
    print(ans)
