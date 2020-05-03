inf = 10**15
mod = 10**9+7
n,m = map(int, input().split())
h = list(map(int, input().split()))
judge = [1 for i in range(n)]
for i in range(m):
    a,b = map(int, input().split())
    if h[a-1] > h[b-1]:
        judge[b-1] = 0
    elif h[b-1] > h[a-1]:
        judge[a-1] = 0
    else:
        judge[b - 1] = 0
        judge[a - 1] = 0
print(sum(judge))