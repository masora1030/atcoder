inf = 10**15
mod = 10**9+7
a,b,n = map(int, input().split())
x = 0
if n >= b:
    x = b-1
else:
    x = n
print((x*a)//b)