import math
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    a,b=lr()
    tmp=1/math.sqrt(a**2+b**2)
    print(tmp*a, tmp*b)


if __name__ == '__main__':
    main()
