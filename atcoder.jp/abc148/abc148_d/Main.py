n = int(input())
a = list(map(int, input().split()))
ans = 0
count = 1
for i in a:
    if i == count:
        count+=1
    else:
        ans+=1
if count == 1:
    print(-1)
else:
    print(ans)