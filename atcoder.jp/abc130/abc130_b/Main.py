# B
n,x = map(int, input().split())
d = 0
count = 1
l = list(map(int, input().split()))
for i in range(n):
    d += l[i]
    if d <= x:
        count+=1
print(count)