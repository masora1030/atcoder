n,m = map(int, input().split())
judge = [i for i in range(1, m+1)]
ans = [1 for i in range(m)]
for i in range(n):
    a = list(map(int, input().split()))
    a.pop(0)
    for j in judge:
        if not j in a:
            ans[j-1] = 0
print(sum(ans))