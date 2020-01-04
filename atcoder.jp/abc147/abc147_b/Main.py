s = input()
ans = 0
n = len(s)
for i in range(n//2):
    if s[i] != s[n-1-i]:
        ans+=1
print(ans)