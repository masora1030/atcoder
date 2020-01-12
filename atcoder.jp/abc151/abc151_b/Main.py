n,k,m = map(int, input().split())
a = list(map(int, input().split()))
mean = 0
mo = m*n
for i in range(n-1):
    mean+=a[i]
if mo <= mean:
    print(0)
elif mo <= k+mean:
    print(mo-mean)
else:
    print(-1)