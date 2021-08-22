import sys
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    n,m = lr()
    a = lr()
    t = lr()
    dic = {}
    for ind,num in enumerate(a):
        if num in dic:
            dic[num].append(ind)
        else:
            dic[num] = [ind]
    ans = m
    now_ind = 0
    init_d = 0
    for num in t:
        if not num in dic:
            print("-1")
            sys.exit()
    init = a[0]
    flg = False
    for num in a:
        if num != init:
            flg = True
    if not flg:
        print(ans)
        sys.exit()
    if init == 0:
        ind1 = dic[1][0]
        ind2 = dic[1][-1]
        init_d = ind1
        if ind1 > n-ind2:
            init_d = n-ind2
    else:
        ind1 = dic[0][0]
        ind2 = dic[0][-1]
        init_d=ind1
        if ind1>n-ind2:
            init_d=n-ind2
    pre = init
    init_flg = True
    for num in t:
        if pre != num:
            if init_flg:
                ans+=init_d
                init_flg = False
            else:
                ans+=1
            pre = num
    print(ans)
