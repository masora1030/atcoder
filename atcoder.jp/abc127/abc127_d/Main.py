inf = 10**15
mod = 10**9+7
n,m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans=0
bc = [list(map(int, input().split())) for i in range(m)]
bc.sort(key=lambda x:x[1])
for i in range(n):
    if bc and a[-1] >= bc[-1][1]:
        ans+=a.pop()
    else:
        if bc and bc[-1][0] != 0:
            bc[-1][0]-=1
            ans+=bc[-1][1]
        elif bc:
            bc.pop()
            if bc and a[-1] >= bc[-1][1]:
                ans += a.pop()
            elif bc:
                bc[-1][0]-=1
                ans+=bc[-1][1]
            else:
                ans+=a.pop()
        else:
            ans += a.pop()
print(ans)