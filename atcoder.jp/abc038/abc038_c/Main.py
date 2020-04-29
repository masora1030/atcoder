inf = 10**15
mod = 10**9+7
n = int(input())
a = list(map(int, input().split()))
count=0
right=0
for left in range(n):
    if left==right:
        right+=1
    while right<n and a[right-1] < a[right]:
        right+=1
    count+=((right-1)-left)
count+=n
print(count)