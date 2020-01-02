a,b,k = map(int, input().split())
if a>=k: print('{} {}'.format(a-k, b))
elif b>=k-a: print('{} {}'.format(0, b-k+a))
else: print('{} {}'.format(0, 0))