sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353


def main():
    n,w=lr()
    a=lr()
    sets=set()
    for i in range(n):
        x=a[i]
        sets.add(x)
        for j in range(i+1,n):
            if j != i:
                y=a[j]
                sets.add(x+y)
                for k in range(j+1, n):
                    if k != i and k != j:
                        z=a[k]
                        sets.add(x+y+z)
    sorted_list = sorted(sets)
    ans=0
    for num in sorted_list:
        if num <= w:
            ans+=1
        else:
            break
    print(ans)

if __name__=='__main__':
    main()