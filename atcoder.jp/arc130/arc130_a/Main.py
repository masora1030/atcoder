sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=2**30-1
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    n=ir()
    s=sr()
    pre=''
    lis = []
    tmp = 1
    for c in s:
        if c == pre:
            tmp+=1
        else:
            lis.append(tmp)
            tmp = 1
        pre = c
    lis.append(tmp)
    ans=0
    for v in lis:
        ans+=v*(v-1)//2
    print(ans)