a,b = map(int, input().split())
if a%2 == 0:
    if (b-a)%4 == 0:
        print(b)
    elif (b-a)%4 == 1:
        print(1)
    elif (b-a)%4 == 2:
        print(b+1)
    else :
        print(0)
else:
    if (b-a-1)%4 == 0:
        print(a^b) # aとbの排他的論理和
    elif (b-a-1)%4 == 1:
        print(a^1) # aと1の排他的論理和
    elif (b-a-1)%4 == 2:
        print(a^(b+1)) # aとb+1の排他的論理和
    else:
        print(a) # aと0の排他的論理和