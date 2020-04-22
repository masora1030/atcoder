inf = 10**9+7
mod = 10**9+7
n = int(input())
a = list(map(int, input().split()))
maxa = max(a)
a.remove(maxa)
if maxa < sum(a):
    print('Yes')
else:
    print('No')