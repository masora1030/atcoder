inf = 10**15
mod = 10**9+7
s = input()
n = len(s)-1
ans = 0
for i in range(2**n):
    acc = int(s[0])
    for j in range(n):
        if ((i >> j) & 1):  # 1だったら(オンだったら)
            ans+=acc
            acc=int(s[j+1])
        else:
            acc *= 10
            acc += int(s[j+1])
    ans+=acc
print(ans)