#最大公約数、最小公倍数、階乗
import fractions
n = int(input())
a = list(map(int, input().split()))

def calcGCDr():
    R = [0 for i in range(n+1)]
    R[n] = 0
    for i in range(1,n+1):
        R[n-i] = fractions.gcd(R[n-i+1],a[n-i])
    return R

def calcGCDl():
    L = [0 for i in range(n+1)]
    L[0] = 0
    for i in range(n):
        L[i+1] = fractions.gcd(L[i],a[i])
    return L

R = calcGCDr()
L = calcGCDl()
max_ans = 1
for i in range(n):
    pre_ans = fractions.gcd(L[i], R[i+1])
    max_ans = max(pre_ans, max_ans)

print(max_ans)