n = int(input())
a = list(map(int, input().split()))
pre = 0
onef = False
twef = False
badf = False
for i,num in enumerate(a):
    if i+1 != num:
        if not onef:
            onef = True
            badf = True
        elif not twef:
            twef = True
            badf = False
        else:
            badf = True
if not badf:
    print('YES')
else:
    print('NO')