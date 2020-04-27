import math
inf = 10**15
mod = 10**9+7
n = int(input())
def distance(x1, y1, x2, y2):
    return (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)

p = [list(map(int, input().split())) for i in range(n)]
ans = -inf
for i in range(n-1):
    x1, y1 = p[i]
    for j in range(i+1, n):
        x2,y2 = p[j]
        ans = max(ans, distance(x1, y1, x2, y2))
print(math.sqrt(ans))
