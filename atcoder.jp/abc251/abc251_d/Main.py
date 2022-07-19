sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353


def main():
    w=ir()
    ans=[]
    for i in range(1,100):
        if i <= w:
            ans.append(i)
        tmp = i*100
        if tmp<=w:
            ans.append(tmp)
        tmp = i*10000
        if tmp <= w:
            ans.append(tmp)
    print(len(ans))
    print(*ans, sep=' ')

if __name__=='__main__':
    main()
