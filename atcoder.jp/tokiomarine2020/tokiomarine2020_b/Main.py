inf = 10**18
mod = 10**9+7

a,v = map(int, input().split())
b,w = map(int, input().split())
t = int(input())
if v-w <= 0:
    print('NO')
else:
    if t >= abs(a-b)/(v-w):
        print('YES')
    else:
        print('NO')