sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    h,w,c,q = lr()
    dic_h = {}
    dic_w = {}
    tnc = []
    h_ind = 0
    w_ind = 0
    for _ in range(q):
        t,n,cc = lr()
        if t == 1:
            if not n in dic_w:
                dic_w[n] = w_ind
                w_ind+=1
            tnc.append([t, dic_w[n], cc-1])
        else:
            if not n in dic_h:
                dic_h[n] = h_ind
                h_ind+=1
            tnc.append([t, dic_h[n], cc-1])
    tnc.reverse()
    visited_h = [False for _ in range(h_ind)]
    visited_w = [False for _ in range(w_ind)]
    ret_h = h
    ret_w = w
    ans = [0 for _ in range(c)]
    for t,n,cc in tnc:
        if t == 1:
            if visited_w[n]:
                continue
            else:
                visited_w[n] = True
                ans[cc]+=ret_w
                ret_h-=1
        else:
            if visited_h[n]:
                continue
            else:
                visited_h[n] = True
                ans[cc]+=ret_h
                ret_w-=1
    print(*ans, sep=" ")