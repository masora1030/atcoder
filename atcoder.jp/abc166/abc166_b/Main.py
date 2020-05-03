inf = 10**15
mod = 10**9+7
n,k = map(int, input().split())
judge = [1 for i in range(n)]
for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for num in a:
        judge[num-1] = 0
print(sum(judge))