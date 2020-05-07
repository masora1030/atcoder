inf = 10**15
mod = 10**9+7
a,b = map(int, input().split())
import fractions

f=fractions.gcd(a,b)           #最大公約数

def factorization(n):
    arr = []
    temp = n
    if n == 1:
        return arr

    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

arr = factorization(f)
print(len(arr)+1)