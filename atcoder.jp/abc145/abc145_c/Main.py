import math
n = int(input())
p = {}
for i in range(n):
    x,y = map(int, input().split())
    p[i] = (x, y)
ave = 0
for i in range(n):
    for j in range(i+1,n):
        ave += math.sqrt(abs(p[i][0] - p[j][0])**2 + abs(p[i][1] - p[j][1])**2)
ave /= ((n*(n-1))/2)
total = ave*(n-1)
print(total)