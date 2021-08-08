sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    h,w,n = lr()
    dich = {}
    dicw = {}
    ab = []
    for i in range(n):
        a,b = lr()
        ab.append([a,b,i+1])
    ind_h = 1
    ab.sort()
    for a,b,i in ab:
        if not a in dich:
            dich[a] = ind_h
            ind_h+=1
    ab.sort(key=lambda x:x[1])
    ind_w=1
    for a, b, i in ab:
        if not b in dicw:
            dicw[b]=ind_w
            ind_w+=1
    ab.sort(key=lambda x:x[2])
    for a,b,_ in ab:
        print(dich[a], dicw[b])