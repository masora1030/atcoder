inf = 10 ** 18
mod = 10 ** 9 + 7

s = input()
t = input()
ans = 0
for i in range(len(s)):
    if s[i] != t[i]:
        ans+=1
print(ans)