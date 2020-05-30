inf = 10 ** 15
mod = 10 ** 9 + 7
t = input()
s = []
for c in t:
    if c == '?':
        s.append('D')
    else:
        s.append(c)
print(*s, sep='')