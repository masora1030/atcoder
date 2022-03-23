sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

import sys

inf=10**18
# mod = 10**9+7
mod=998244353

if __name__=='__main__':
    n,k = lr()
    a=lr()
    a.sort(reverse=True)
    hws = []
    pre_h = 0
    now_w = 0
    for num in a:
        if num != pre_h:
            hws.append([pre_h, now_w])
            now_w = 1
            pre_h = num
        else:
            now_w+=1
    hws.append([pre_h, now_w])
    hws.append([0,0])
    ret = k
    ans = 0
    now_w = 0
    for i in range(1, len(hws)-1):
        h,w = hws[i]
        nh,nw = hws[i+1]
        now_w += w
        sa_h = h-nh
        if ret >= sa_h*now_w:
            ret -= sa_h*now_w
            ans += (h+(nh+1))*sa_h//2*now_w
        else:
            tmp = ret//now_w
            nh = h-tmp
            ans+=(h+(nh+1))*tmp//2*now_w
            tmp = ret%now_w
            ans+=nh*tmp
            break
    print(ans)
