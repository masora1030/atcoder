sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    n,l=lr()
    sets = []
    for i in range(n):
        s=sr()
        tmp=set()
        for c in s:
            tmp.add(c)
        sets.append(tmp)
    ans=0
    pow_nums = []
    for num in range(27):
        pow_nums.append(pow(num,l,mod))
    for i in range(1,2**n):
        use = []
        for j in range(n):
            if (i >> j) & 1:
                use.append(j)
        use_set = sets[use[0]]
        for ind in use:
            use_set = use_set & sets[ind]
        nums=len(use_set)
        ret=pow_nums[nums]
        if len(use)%2==1:
            # add
            ans+=ret
            ans%=mod
        else:
            # sub
            ans-=ret
    print(ans%mod)

if __name__ == '__main__':
    main()
