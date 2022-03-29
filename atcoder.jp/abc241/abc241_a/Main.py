sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    a=lr()
    ans = [0]
    for i in range(10):
        ans.append(a[ans[-1]])
    print(ans[3])


if __name__ == '__main__':
    main()
