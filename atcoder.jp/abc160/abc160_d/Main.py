n,x,y = list(map(int, input().split()))
ans = [0 for i in range(n)]
for i in range(1,n):
    for j in range(i+1,n+1):
        t = min(j-i, abs(x-i)+abs(y-j)+1)
        ans[t]+=1

for k in range(1,n):
    print(ans[k])