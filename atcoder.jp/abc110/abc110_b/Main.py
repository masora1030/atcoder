inf = 10**15
mod = 10**9+7
n,m,x,y = map(int, input().split())
xlist = list(map(int, input().split()))
ylist = list(map(int, input().split()))
xmax = max(xlist)
ymin = min(ylist)
if xmax < ymin and xmax < y and ymin > x:
    print('No War')
else:
    print('War')