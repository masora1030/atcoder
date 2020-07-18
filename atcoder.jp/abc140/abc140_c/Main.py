n = int(input())
b = list(map(int, input().split()))
a = [0 for i in range(n+1)]
a[0] = b[0]
for i in range(n-2):
    a.append(min(b[i], b[i+1]))
a.append(b[-1])
print(sum(a))