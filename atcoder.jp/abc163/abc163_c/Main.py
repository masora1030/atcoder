inf = 10**15
mod = 10**9+7

n = int(input())
a = list(map(int, input().split()))
ans = [0 for i in range(n)]
for num in a:
    ans[num-1] += 1
for ansnum in ans:
    print(ansnum)