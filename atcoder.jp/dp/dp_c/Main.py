# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
inf = 10**9+7

n = int(input())
dp_a = [0 for i in range(n+1)]
dp_b = [0 for i in range(n+1)]
dp_c = [0 for i in range(n+1)]

for i in range(n):
    a,b,c = map(int, input().split())
    dp_a[i+1] = max(dp_b[i]+a, dp_c[i]+a)
    dp_b[i + 1] = max(dp_a[i] + b, dp_c[i] + b)
    dp_c[i + 1] = max(dp_a[i] + c, dp_b[i] + c)
print(max(dp_a[n], dp_b[n], dp_c[n]))