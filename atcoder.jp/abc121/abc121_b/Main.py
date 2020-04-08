n,m,c = map(int, input().split())
ans = 0
b = list(map(int, input().split()))
for i in range(n):
    a = list(map(int, input().split()))
    total = 0
    for j in range(m):
        total+=a[j]*b[j]
    total+=c
    if total > 0:
        ans+=1
print(ans)