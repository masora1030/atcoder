sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

# import numpy as np

if __name__=='__main__':
    n,m = lr()
    t = []
    for i in range(n):
        _ = ir()
        a = set(lr())
        lis=[]
        for j in range(m):
            if j+1 in a:
                lis.append(1)
            else:
                lis.append(0)
        t.append(lis)
    visited = [False for i in range(n)]
    now_rank = 0
    hakidasi = []
    while now_rank < m:
        for i in range(n):
            if not visited[i] and t[i][now_rank] == 1:
                visited[i] = True
                hakidasi.append(t[i])
                for j in range(n):
                    if not visited[j] and t[j][now_rank] == 1:
                        for k in range(now_rank, m):
                            t[j][k] = (t[j][k]+t[i][k])%2
                break
        now_rank+=1
    ans = [0 for i in range(m)]
    now_rank = 0
    ok_flg = True
    target = lr()
    for haki in hakidasi:
        first_1 = -1
        for ind, num in enumerate(haki):
            if num==1:
                first_1 = ind
                break
        for ind in range(now_rank,first_1):
            if ans[ind] != target[ind]:
                ok_flg = False
                break
        if not ok_flg:
            break
        now_rank = first_1
        if now_rank >= m:
            break
        if target[now_rank] != ans[now_rank]:
            for k in range(now_rank, m):
                ans[k] = (haki[k]+ans[k])%2
        now_rank+=1
    for k in range(m):
        if ans[k] != target[k]:
            ok_flg = False
            break
    if ok_flg:
        print(pow(2,n-len(hakidasi),mod))
    else:
        print(0)
