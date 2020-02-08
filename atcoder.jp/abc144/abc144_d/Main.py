import math
a,b,x = map(int, input().split())
h = 2*(a*b-x/a)/a
h2 = 2*(x/a)/b
if x/a > a*b/2:
    atan = math.degrees(math.atan(h/a))
else:
    atan = math.degrees(math.atan(b/h2))
print(atan)