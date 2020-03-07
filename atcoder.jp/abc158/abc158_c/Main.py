# C
a,b = map(int, input().split())
if a > b:
    print(-1)
else:
    a_min, a_max, b_min, b_max = 0,0,0,0
    
    if (a*100)%8 == 0:
        a_min = a/0.08
    else:
        a_min = a/0.08 + 1
    a_max = a_min
    while int(a_max*0.08) == a:
        a_max += 1
    a_max -= 1
    
    b_min = b*10
    b_max = b_min
    while int(b_max*0.1) == b:
        b_max += 1
    b_max -= 1
    
    if b_max >= a_min and a_max >= b_min:
        print(int(max(a_min,b_min)))
    else:
        print(-1)