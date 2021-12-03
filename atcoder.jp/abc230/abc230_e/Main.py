import sys
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# mod = 10**9+7
mod = 998244353

if __name__=='__main__':
    n=ir()
    if n==1:
        print(1)
        sys.exit()
    tmp = 2
    now = n
    ans = n
    while now != 0:
        pre = n//tmp
        if pre == now:
            add = n//now - tmp
            ans += add*(n//tmp)
            now = n//tmp
            ans += now
            tmp = tmp + add + 1
        else:
            ans += n//tmp
            tmp += 1
            now = n//tmp
    print(ans)

