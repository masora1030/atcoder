sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    n=ir()
    a=lr()
    aa=[[num, i] for i,num in enumerate(a)]
    aa.sort()
    print(aa[-2][1]+1)