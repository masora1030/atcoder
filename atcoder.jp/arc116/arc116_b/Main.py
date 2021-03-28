import sys
# from sys import stdin
# readline = stdin.readline
sr = lambda: input()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

inf = 10 ** 18
# mod = 10 ** 9 + 7
mod = 998244353
# len(bin(n)) - bin(n).rfind("1") - 1

if __name__=='__main__':
    n=ir()
    a=lr()
    if n==1:
        print((a[0]**2)%mod)
        sys.exit()
    a.sort()
    ans=0
    for num in a:
        ans+=(num**2)%mod
        ans%=mod
    min_ind = n-1
    tmp = 0
    for min_ind in range(n-2, -1, -1):
        tmp*=2
        tmp%=mod
        tmp+=a[min_ind+1]
        tmp%=mod
        ans+=a[min_ind]*tmp
        ans%=mod
    print(ans)