sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    n,x,y,z=lr()
    a=lr()
    b=lr()
    ab=[[a[i],n-i,b[i]] for i in range(n)]
    ab.sort(key=lambda x:(x[0], x[1]), reverse=True)
    # print(ab)
    ans=[]
    for i in range(x):
        ans.append(n-ab[i][1]+1)
    next_ab = []
    for j in range(x,n):
        next_ab.append([ab[j][2], ab[j][1], ab[j][0]])
    next_ab.sort(key=lambda x: (x[0], x[1]), reverse=True)
    # print(next_ab)
    for i in range(y):
        ans.append(n-next_ab[i][1]+1)
    ab=[]
    for j in range(y, len(next_ab)):
        ab.append([next_ab[j][0], next_ab[j][1], next_ab[j][2]])
    ab.sort(key=lambda x:x[0]+x[2], reverse=True)
    ab.sort(key=lambda x: (x[0]+x[2], x[1]), reverse=True)
    # print(ab)
    for i in range(z):
        ans.append(n-ab[i][1]+1)
    ans.sort()
    for num in ans:
        print(num)

if __name__ == '__main__':
    main()
