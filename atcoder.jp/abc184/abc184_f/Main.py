import sys
import bisect

sr = lambda: input()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

inf = 10 ** 18
# mod = 10 ** 9 + 7
mod = 998244353
# len(bin(n)) - bin(n).rfind("1") - 1

# Press the green button in the gutter to run the script.
if __name__=='__main__':
    n,t = lr()
    a = lr()
    if n == 1:
        if a[0] <= t:
            print(a[0])
        else:
            print(0)
        sys.exit()
    mid = n//2
    fi = []
    se = []
    for i in range(n):
        if i < mid:
            fi.append(a[i])
        else:
            se.append(a[i])
    filen = len(fi)
    selen = len(se)
    fi1, se1 = [], []


    for i in range(2**filen):
        pre = 0
        for j in range(filen):
            if (i >> j) & 1:
                pre+=fi[j]
        fi1.append(pre)

    for i in range(2**selen):
        pre=0
        for j in range(selen):
            if (i >> j) & 1:
                pre+=se[j]
        se1.append(pre)


    se1.sort()
    ans = 0
    selen = len(se1)
    for num in fi1:
        tmp = t-num
        if tmp < 0:
            continue
        ind = bisect.bisect_left(se1, tmp)
        if ind != 0:
            if ind != selen and se1[ind] != tmp:
                ind-=1
            if ind == selen:
                ind-=1
        pre = se1[ind]+num
        ans = max(ans, pre)
    print(ans)