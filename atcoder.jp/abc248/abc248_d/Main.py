import bisect
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    n=ir()
    a=lr()
    num2inds = {}
    for i,num in enumerate(a):
        if num in num2inds:
            num2inds[num].append(i+1)
        else:
            num2inds[num] = [i+1]
    q=ir()
    for i in range(q):
        l,r,x = lr()
        if x in num2inds:
            print(bisect.bisect_left(num2inds[x],r+1) - bisect.bisect_left(num2inds[x],l))
        else:
            print(0)


if __name__ == '__main__':
    main()
