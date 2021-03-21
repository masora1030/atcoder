# from sys import stdin
# readline = stdin.readline
sr = lambda: input()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

inf = 10 ** 18
# mod = 10 ** 9 + 7
mod = 998244353
# len(bin(n)) - bin(n).rfind("1") - 1


if __name__=='__main__':
    n = ir()
    a = [2 for i in range(n)]
    a[0] = 1
    for i in range(2,n):
        tmp = a[i-1]+1
        for j in range(2*i, n+1, i):
            if a[j-1] < tmp:
                a[j-1] = tmp
    print(*a, sep=" ")