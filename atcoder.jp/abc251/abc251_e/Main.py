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
    dp_without_last = [inf for _ in range(n)] # i までに上げる際の最小費用
    dp_without_last[0] = a[0]
    dp_without_last[1] = a[0]
    for i in range(1, n-1):
        # i, i+1に渡すか？
        dp_without_last[i] = min(dp_without_last[i], dp_without_last[i-1]+a[i])
        dp_without_last[i+1] = min(dp_without_last[i+1], dp_without_last[i-1]+a[i])

    dp_with_last=[inf for _ in range(n)]  # i までに上げる際の最小費用
    dp_with_last[0] = a[-1]
    dp_with_last[-1] = a[-1]
    for i in range(n-1):
        # i, i+1に渡すか？
        dp_with_last[i]=min(dp_with_last[i], dp_with_last[i-1]+a[i])
        dp_with_last[i+1]=min(dp_with_last[i+1], dp_with_last[i-1]+a[i])

    print(min(dp_without_last[-1], dp_with_last[-2]))


if __name__=='__main__':
    main()
