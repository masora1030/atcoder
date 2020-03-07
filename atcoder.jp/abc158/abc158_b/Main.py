# B
n,a,b  = map(int, input().split())
if n%(a+b) <= a:
    print(a*(n//(a + b)) + n%(a+b))
else:
    print(a*(n//(a + b)) + a)