x1,y1,r = map(int, input().split())
x2,y2,x3,y3 = map(int, input().split())
fr = True
fb = True
if (x1 -r) <= x2 and x3 <= (x1+r) and (y1 - r) <= y2 and y3 <= (y1 + r):
    if (x1 - x2)**2 + (y1 - y2)**2 <= r**2:
        if (x1 - x2)**2 + (y1 - y3)**2 <= r**2:
            if (x1 - x3)**2 + (y1 - y2)**2 <= r**2:
                if (x1 - x3)**2 + (y1 - y3)**2 <= r**2:
                    fb = False
 
if (x1 - r) >=x2 and (x1+r) <= x3:
    if (y1-r) >= y2 and (y1 + r) <= y3:
        fr = False
 
print("YES" if fr else "NO")
print("YES" if fb else "NO")