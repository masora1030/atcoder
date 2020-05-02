inf = 10**15
mod = 10**9+7
k = int(input())
a,b = map(int, input().split())
tmp = a//k
if tmp*k == a:
    print('OK')
elif (tmp+1)*k <= b:
    print('OK')
else:
    print('NG')