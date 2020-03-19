# B
n,l = map(int,input().split())
ans=0
for i in range(1,n+1):
    ans+=(l+i-1)
if l+n-1 < 0:
    print(ans-(l+n-1))
elif l+n-1 >= 0 and l <= 0:
    print(ans)
else:
    print(ans-l)