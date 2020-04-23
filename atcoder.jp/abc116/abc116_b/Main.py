s = int(input())
m = 1
if s == 1:
    print(4)
elif s == 2:
    print(4)
else:
    while 1:
        if s == 1:
            break
        if s % 2 == 0:
            s = s // 2
            m += 1
        else:
            s = 3*s+1
            m += 1
    m += 1
    print(m)