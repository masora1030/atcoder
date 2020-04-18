# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
import sys
inf = 10**9+7
mod = 10**9+7

a,b,c,x,y = map(int, input().split())
ans = a*x + b*y
if a < b:
    a,b = b,a
    x,y = y,x
if x > y:
    ans = min(a*x + b*y, 2*c*y + min(2*(x-y)*c, a*abs(x-y)))
else:
    ans = min(a*x + b*y, 2*c*x + min(2*(y-x)*c, b*abs(x-y)))
print(ans)