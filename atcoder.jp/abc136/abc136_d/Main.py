# D
s = str(input())
RLlist = []
i = 0
length = len(s)
Rcount=0
Lcount=0
RLplace=-1
ans = [0 for i in range(length)]
while i < length:
    Rcount=0
    while i < length and s[i] == 'R':
        Rcount+=1
        i+=1
    if i < length and s[i] == 'L':
        RLplace = i-1
        Lcount=0
    while i < length and s[i] == 'L':
        Lcount+=1
        i+=1
    RLlist.append((RLplace, Rcount, Lcount))

for t in RLlist:
    if t[1]%2 == 0 and t[2]%2 == 0:
        ans[t[0]]+=(t[1]//2 + t[2]//2)
        ans[t[0]+1]+=(t[1]//2 + t[2]//2)
    elif t[1]%2 != 0 and t[2]%2 == 0:
        ans[t[0]]+=(t[1]//2 + 1 + t[2]//2)
        ans[t[0]+1]+=(t[1]//2 + t[2]//2)
    elif t[1]%2 == 0 and t[2]%2 != 0:
        ans[t[0]]+=(t[1]//2 + t[2]//2)
        ans[t[0]+1]+=(t[1]//2 + 1 + t[2]//2)
    else:
        ans[t[0]]+=(t[1]//2 + 1 + t[2]//2)
        ans[t[0]+1]+=(t[1]//2 + 1 + t[2]//2)
print(*ans ,sep=' ')