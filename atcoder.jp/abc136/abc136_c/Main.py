# C
n = int(input())
h = list(map(int, input().split()))
ans = True
pre = -1
for num in h:
    if num > pre:
        pre = num-1
    elif num == pre:
        pre = num
    else:
        ans = False
        break
if ans:
    print('Yes')
else:
    print('No')