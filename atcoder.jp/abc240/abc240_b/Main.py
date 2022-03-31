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
    s=set()
    for num in a:
        s.add(num)
    print(len(s))

if __name__ == '__main__':
    main()
