# D
n = int(input())
y = list(map(int, input().split()))
for i,num in enumerate(y):
    if i % 2 == 1:
        y[i] = -y[i]

a2=[0]
for i in y:a2.append(a2[-1]+i)
def SumArea(r, l):
    return a2[l]-a2[r]
    
ans = [0 for i in range(n)]
for i in range(n):
    count=0
    if i % 2 == 1:
        count -= SumArea(i, n)
        count += SumArea(0, i)
    else:
        count += SumArea(i, n)
        count -= SumArea(0, i)
    ans[i] = count
print(*ans, sep=' ')