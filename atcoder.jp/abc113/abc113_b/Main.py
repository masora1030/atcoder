import sys
inf = 10**15
mod = 10**9+7
n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
bi = []
bii = []
for i in range(n):
    bi.append(t-h[i]*0.006)
    bii.append([t-h[i]*0.006, i+1])
bi.sort()
import bisect
ind = bisect.bisect_left(bi, a)
tmp = 0
if ind == n:
    tmp = bi[n-1]
else:
    if abs(bi[ind]-a) > abs(bi[ind-1]-a):
        tmp = bi[ind-1]
    else:
        tmp = bi[ind]
for i in range(n):
    if tmp == bii[i][0]:
        print(bii[i][1])
        sys.exit()