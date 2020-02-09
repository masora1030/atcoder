s,t = map(str, input().split())
a,b = map(int, input().split())
u = input()
if u == s:
    print('{} {}'.format(a-1,b))
if u == t:
    print('{} {}'.format(a,b-1))