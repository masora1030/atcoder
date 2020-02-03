n = int(input())
P = list(map(int, input().split()))
count = 0
min = 10**12
for i in range(n):
    if P[i] <= min:
        count+=1
        min = P[i]
print(count)