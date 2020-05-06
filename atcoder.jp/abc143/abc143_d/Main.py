import bisect
inf = 10**15
mod = 10**9+7
n = int(input())
l = list(map(int, input().split()))
l.sort()
ans=0
for i in range(n-2):
    a = l[i]
    for j in range(i+1, n-1):
        b = l[j]
        indc = bisect.bisect_left(l,a+b)
        ans+=(indc-j-1)
print(ans)