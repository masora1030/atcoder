import itertools

sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    N = input().split()
    s = list(N[0])
    k = int(N[1])
    len_s = len(s)
    a = list(itertools.permutations(s, len_s))
    a.sort()
    ind = 0
    ans = 0
    ans_ind = 0
    pre = [-1 for i in range(len_s)]
    while ans < k:
        now = a[ind]
        flg = False
        for j in range(len_s):
            if now[j] != pre[j]:
                flg = True
        if flg:
            ans+=1
            ans_ind=ind
            pre = now
        ind+=1
    print(''.join(a[ans_ind]))
