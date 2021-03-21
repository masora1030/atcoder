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
    c = [lr() for i in range(n)]
    b = [0]
    a = [c[0][0]]
    for j in range(n-1):
        b.append(b[-1]+c[0][j+1]-c[0][j])

    flg = True
    for i in range(n-1):
        tmp = c[i+1][0]-c[i][0]
        aa = a[-1]+tmp
        a.append(aa)
        for j in range(n):
            if c[i+1][j] != aa+b[j]:
                flg = False
                break
        if not flg:
            break
    if flg:
        min_a = min(a)
        min_b = min(b)
        if min_a >= 0 and min_b >= 0:
            print("Yes")
            print(*a, sep=" ")
            print(*b, sep=" ")
        elif min_a < 0 and min_b+min_a >= 0:
            for i in range(n):
                a[i]-=min_a
                b[i]+=min_a
            print("Yes")
            print(*a, sep=" ")
            print(*b, sep=" ")
        elif min_b < 0 and min_a+min_b >= 0:
            for i in range(n):
                b[i]-=min_b
                a[i]+=min_b
            print("Yes")
            print(*a, sep=" ")
            print(*b, sep=" ")
        else:
            print("No")
    else:
        print("No")