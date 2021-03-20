import math

def get_primenumber(number):
    prime_list = []
    search_list = list(range(2,number+1))
    while True:
      if search_list[0] > math.sqrt(number):
        prime_list.extend(search_list)
        break
      else:
        head_num = search_list[0]
        prime_list.append(head_num)
        search_list.pop(0)
        search_list = [num for num in search_list if num % head_num != 0]
    return prime_list

arrr = get_primenumber(10**5)

def factorization(n):
    arr = []
    temp = n
    if n == 1:
        return arr

    for i in arrr:
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
        if i*i > n:
            break

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


from sys import stdin
readline = stdin.readline
sr = lambda: readline()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

inf = 10 ** 18
# mod = 10 ** 9 + 7
mod = 998244353
# len(bin(n)) - bin(n).rfind("1") - 1

if __name__=='__main__':
    a,b = lr()
    c,d = lr()
    print(b-c)