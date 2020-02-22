n,k = map(int, input().split())
count = 1
tmp = k
while tmp <= n:
    count+=1
    tmp = tmp*k
print(count)