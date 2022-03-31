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
    if a==1 and b==10:
        print("Yes")
    elif b-a == 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
