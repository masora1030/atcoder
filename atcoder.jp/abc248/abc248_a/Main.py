sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    ss=set(str(num) for num in range(10))
    s=sr()
    for c in s:
        ss.remove(c)
    print(ss.pop())

if __name__ == '__main__':
    main()
