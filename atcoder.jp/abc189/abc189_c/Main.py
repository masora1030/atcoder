sr = lambda: input()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

inf = 10 ** 18
# mod = 10 ** 9 + 7
mod = 998244353
# len(bin(n)) - bin(n).rfind("1") - 1

# Press the green button in the gutter to run the script.
if __name__=='__main__':
    n = ir()
    a = lr()
    min_a = [num for num in a]
    for i in range(n):
        num = a[i]
        for j in range(i):
            min_a[j] = min(min_a[j], num)
            a[j] = max(min_a[j]*(i-j+1), a[j])
    print(max(a))