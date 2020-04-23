n = int(input())
h = list(map(int, input().split()))
maxh = max(h)
ans = 0
for j in range(maxh):
    countnow = False
    for i in range(n):
        if h[i] != 0:
            h[i] -= 1
            if not countnow:
                ans+=1
                countnow=True
        else:
            countnow = False
print(ans)