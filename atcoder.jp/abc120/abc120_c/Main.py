stack = []
s = input()
ans = 0
for c in s:
    if stack:
        tmp = stack.pop()
        if c == tmp:
            stack.append(tmp)
            stack.append(c)
        else:
            ans+=2
    else:
        stack.append(c)
print(ans)