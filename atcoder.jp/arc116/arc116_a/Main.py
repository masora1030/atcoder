sr = lambda: input()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

inf = 10 ** 18
# mod = 10 ** 9 + 7
mod = 998244353
# len(bin(n)) - bin(n).rfind("1") - 1

if __name__=='__main__':
    test=ir()
    for t in range(test):
        n = ir()
        if n%2 == 1:
            print('Odd')
        else:
            if n%4==0:
                print('Even')
            else:
                print('Same')