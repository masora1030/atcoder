sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    n=ir()
    a=[lr() for i in range(3)]
    dp = [[0 for i in range(46)] for j in range(3)]
    for i in range(3):
        for num in a[i]:
            dp[i][num%46]+=1
    ans = 0
    for k,num in enumerate(dp[0]):
        ret = 46-k
        for l,num2 in enumerate(dp[1]):
            ret2 = (ret-l)%46
            ans += num*num2*dp[2][ret2]
    print(ans)