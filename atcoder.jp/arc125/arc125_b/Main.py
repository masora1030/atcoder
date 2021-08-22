sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    n=ir()
    ans=int(n**(1/2))
    max_n = int(n**(1/2))+1
    for i in range(1,max_n):
        if i%2 == 1:
            # i+2 から n//i までの奇数の数
            max_k = min(n//i, 2*n-i)
            max_i = i+1
            if max_k%2 == 0:
                ans+=max_k//2
            else:
                ans+=max_k//2+1
            if max_i%2 == 0:
                ans-=max_i//2
            else:
                ans-=max_i//2+1
        else:
            # i+2 から n//i までの偶数の数
            max_k = min(n//i, 2*n-i)
            max_i = i+1
            if max_k%2 == 0:
                ans+=max_k//2
            else:
                ans+=max_k//2
            if max_i%2 == 0:
                ans-=max_i//2
            else:
                ans-=max_i//2
        ans%=mod
    print(ans)
