sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353

num_l = 0

def main():
    a = sr().split()
    aa = ''.join(a[:2])
    bb = ''.join(a[2:])
    if aa <= bb:
        print("Takahashi")
    else:
        print("Aoki")



if __name__ == '__main__':
    main()
