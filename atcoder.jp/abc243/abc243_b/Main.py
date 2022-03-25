sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

import sys

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    n=ir()
    a=lr()
    b=lr()
    ans1=0
    ans2=0
    dica = {}
    dicb={}
    for i in range(n):
        x = a[i]
        y = b[i]
        if x==y:
            ans1+=1
        if x in dica:
            dica[x] +=1
        else:
            dica[x] = 1
        if y in dicb:
            dicb[y] +=1
        else:
            dicb[y] = 1
    for k,v in dicb.items():
        if k in dica:
            ans2 += min(v, dica[k])
    ans2-=ans1
    print(ans1)
    print(ans2)
if __name__ == '__main__':
    main()
