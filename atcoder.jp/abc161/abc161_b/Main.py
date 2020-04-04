n,m = map(int, input().split())
a = list(map(int, input().split()))
count = 0
lim = sum(a)/(4*m)
for num in a:
    if num >= lim:
        count+=1
if count >= m:
    print('Yes')
else:
    print('No')