inf = 10 ** 15
mod = 10 ** 9 + 7
a,b = map(int, input().split())
if a*b % 2 == 0:
    print('No')
else:
    print('Yes')