sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    n,m=lr()
    a=lr()
    b=lr()
    dica = {}
    for num in a:
        if num in dica:
            dica[num]+=1
        else:
            dica[num]=1
    flg=True
    for num in b:
        if not num in dica:
            flg=False
            break
        else:
            if dica[num]:
                dica[num]-=1
            else:
                flg=False
                break
    if flg:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
