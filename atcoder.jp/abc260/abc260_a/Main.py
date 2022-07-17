import sys
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    s=sr()
    c2num = {}
    for c in s:
        if c in c2num:
            c2num[c]+=1
        else:
            c2num[c]=1
    for c,v in c2num.items():
        if v==1:
            print(c)
            sys.exit()
    print(-1)


if __name__ == '__main__':
    main()