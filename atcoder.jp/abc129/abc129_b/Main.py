n = int(input())
w = list(map(int, input().split()))
# 累積和
a2=[0]
for i in w:a2.append(a2[-1]+i)
def SumArea(l, r):
    return a2[l]-a2[r]

minnum = 10**9+7

for i in range(n+1):
    tmp = abs(SumArea(i, n) - SumArea(0, i))
    if tmp < minnum:
        minnum = tmp
    
print(minnum)