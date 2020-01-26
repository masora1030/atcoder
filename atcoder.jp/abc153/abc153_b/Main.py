h,n = map(int, input().split())
a = list(map(int, input().split()))
total = 0
for i in range(n):
    total += a[i]
if total >= h:
    print('Yes')
else:
    print('No')