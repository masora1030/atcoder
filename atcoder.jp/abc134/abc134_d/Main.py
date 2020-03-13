# D
n = int(input())
a = list(map(int, input().split()))
ans = [0 for i in range(n+1)]
a.reverse()
for i,num in enumerate(a):
    sum_a = 0
    for j in range(0, n+1, (n-i)):
        sum_a += ans[j]
    if sum_a%2 == 0:
        if num == 1:
            ans[n-i] = 1
    else:
        if num == 0:
            ans[n-i] = 1
sum_ans = 0
ansprint = []
for i,num in enumerate(ans):
    if num == 1:
        ansprint.append(i)
        sum_ans+=1
print(sum_ans)
print(*ansprint, sep=' ')

