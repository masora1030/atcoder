# 約数生成
def make_divisors(a,b):
    divisors = []
    for i in range(1, a+1):
        if a % i == 0:
            if b % i == 0:
                divisors.append(i)

    divisors.sort(reverse=True)
    return divisors
a,b,k = map(int, input().split())
y = make_divisors(a,b)
print(y[k-1])