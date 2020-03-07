n = int(input())
h = list(map(int, input().split()))
ans = 0
i = 0
while i < n-1:
    k = 0
    while h[i] >= h[i+1]:
        k+=1
        i+=1
        if i >= n-1: break
    if k > ans:
        ans = k
    i+=1
print(ans)