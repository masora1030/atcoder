sr = lambda: input()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))


inf = 10 ** 18
# mod = 10 ** 9 + 7
mod = 998244353
# len(bin(n)) - bin(n).rfind("1") - 1

# Press the green button in the gutter to run the script.
if __name__=='__main__':
    n=ir()
    a = lr()
    ans = 0
    for num in a:
        ans += (len(bin(num)) - bin(num).rfind("1") - 1)
    print(ans)