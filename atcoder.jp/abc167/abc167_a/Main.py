inf = 10**15
mod = 10**9+7

s = input()
t = list(input())
t.pop()
t = ''.join(t)
if s == t:
    print('Yes')
else:
    print('No')