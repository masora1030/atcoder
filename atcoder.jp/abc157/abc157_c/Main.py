# C
f = True
n,m = map(int, input().split())
num = [-1 for i in range(n)]
for i in range(m):
    s,c = map(int, input().split())
    if num[s-1] == -1:
        num[s-1] = c
    else:
        if num[s-1] != c:
            f = False
if f:
    if n == 1:
        if  num[0] == -1:
            print(0)
        else:
            print(num[0])
    elif n == 2:
        if num[0] == 0:
            print(-1)
        elif num[0] == -1:
            if num[1] == -1:
                print(10)
            else:
                print(10 + num[1])
        else:
            if num[1] == -1:
                print(num[0]*10)
            else:
                print(num[0]*10 + num[1])
    elif n == 3:
        if num[0] == 0:
            print(-1)
        elif num[0] == -1:
            if num[1] == -1:
                if num[2] == -1:
                    print(100)
                else:
                    print(100 + num[2])
            else:
                if num[2] == -1:
                    print(100 + num[1]*10)
                else:
                    print(100 + num[1]*10 + num[2])
        else:
            if num[1] == -1:
                if num[2] == -1:
                    print(num[0]*100)
                else:
                    print(num[0]*100 + num[2])
            else:
                if num[2] == -1:
                    print(num[0]*100 + num[1]*10)
                else:
                    print(num[0]*100 + num[1]*10 + num[2])
else:
    print(-1)