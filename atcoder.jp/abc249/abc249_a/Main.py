sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353


def main():
    a,b,c,d,e,f,x = lr()
    t=(x//(a+c)*a + min(a,x%(a+c)))*b
    g=(x//(d+f)*d + min(d,x%(d+f)))*e
    if t > g:
        print("Takahashi")
    elif t==g:
        print("Draw")
    else:
        print("Aoki")

if __name__=='__main__':
    main()
