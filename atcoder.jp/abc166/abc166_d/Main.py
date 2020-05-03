import sys
inf = 10**15
mod = 10**9+7
x = int(input())
for i in range(-10**5, 10**5+1):
    tmp = i**5-x
    b = int(abs(tmp)**(1/5))
    if b**5 == abs(tmp):
        if tmp > 0:
            print('{} {}'.format(i, b))
        else:
            print('{} {}'.format(i, -b))
        sys.exit()