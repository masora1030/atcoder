import sys

# sys.setrecursionlimit(10**4)
# from sys import stdin
# readline = stdin.readline
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
mod=10**9+7
# mod = 998244353

if __name__=='__main__':
    n=ir()
    a=lr()
    max_a = [a[0]]
    sum_a = [a[0]]
    for num in a[1:]:
        max_a.append(max(num, max_a[-1]))
        sum_a.append(sum_a[-1]+num)
    ans = a[0]*2
    for k in range(n-1):
        print(ans)
        ans-=max_a[k]*(k+1)
        ans+=max_a[k+1]*(k+2)
        ans+=sum_a[k+1]
    print(ans)