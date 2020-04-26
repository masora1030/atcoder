n = int(input())
s = []
for i in range(n):
    s.append(input())
s.sort()
ans = 0
pre = ''
for i in range(n):
    if s[i] != pre:
        ans+=1
        pre = s[i]
print(ans)