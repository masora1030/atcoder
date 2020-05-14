def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors
ans = []
n = int(input())
for i in range(3,200,2):
    tmp = len(make_divisors(i))
    if tmp == 8:
        ans.append(i)
m = 0
for tmp in ans:
    if tmp <= n:
        m+=1
print(m)