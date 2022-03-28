sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    a,b,c,x = lr()
    if x <= a:
        print(1)
    elif x <= b:
        print(c/(b-a))
    else:
        print(0)

if __name__ == '__main__':
    main()
