inf = 10 ** 15
mod = 10 ** 9 + 7
n = int(input())
d = [int(input()) for i in range(n)]
maxnum = sum(d)
minnum = inf
if n == 1:
    minnum = d[0]
elif n == 2:
    minnum = abs(d[0]-d[1])
else:
    flag = True
    tmp = 0
    for num in d:
        if num > maxnum - num:
            flag = False
            tmp = max(tmp, num)
    if flag:
        minnum = 0
    else:
        minnum = abs(2*tmp-maxnum)
print(maxnum)
print(minnum)
print()