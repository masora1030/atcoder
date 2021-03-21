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
    n,m = lr()
    s = [sr() for i in range(n)]
    even = 0
    odd = 0
    for c in s:
        if sum(list(map(int, list(c[:-1]))))%2 == 0:
            even+=1
        else:
            odd+=1
    print(even*odd)