def lcm(a,m):
    from fractions import gcd
    x = a[0]
    for i in range(1, len(a)):
        
        x = (x * a[i]) // gcd(x, a[i])
        if x > m:
            return m+1
    return x

def count2div(n):
    count=0
    while not n%2:
        n/=2
        count+=1
    return count

n,m = map(int, input().split())
a = list(map(int, input().split()))
b = [i//2 for i in a]
c = [0 for i in a]
b_f = True
for i in range(n):
    c[i] = count2div(b[i])
for i in range(n-1):
    if c[i] != c[i+1]:
        b_f = False
lcm = lcm(b,m)
i=1
count=0
if m >= lcm:
    m-=lcm
    count = m//(lcm*2) + 1
if b_f:
    print(count)
else:
    print(0)