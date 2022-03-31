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
    stack = []
    ans=0
    for num in a:
        if not stack:
            stack.append([num,1])
            ans+=1
            print(ans)
            continue
        if stack[-1][0] == num:
            stack[-1][1]+=1
            ans+=1
            if stack[-1][1] == num:
                k,v = stack.pop()
                ans-=v
            print(ans)
        else:
            stack.append([num,1])
            ans+=1
            print(ans)

if __name__ == '__main__':
    main()
