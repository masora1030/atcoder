x,y = map(int, input().split())
if y%2 == 1:
    print('No')
else:
    if x >= (y-2*x)/2 >= 0:
        print('Yes')
    else:
        print('No')