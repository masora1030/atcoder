inf = 10 ** 15
mod = 10 ** 9 + 7

n = int(input())
tmp = 0
flag = False
while tmp <= n:
    if (n-tmp) % 7 == 0:
        flag = True
    tmp+=4
if flag:
    print('Yes')
else:
    print('No')