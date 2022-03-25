sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

import sys

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    v,a,b,c = lr()
    total = a+b+c
    ret = v%total
    if ret < a:
        print("F")
    elif ret < a+b:
        print("M")
    else:
        print("T")

if __name__ == '__main__':
    main()
