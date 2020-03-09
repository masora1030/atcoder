# B
n = int(input())
a = list(map(int, input().split()))
div = 0
for i in range(n):
    div += 1/a[i]
ans = 1/div
print(ans)