inf = 10 ** 18
mod = 10 ** 9 + 7

s = list(input().split())
n = int(input())
t = [input() for i in range(n)]
for g,c in enumerate(s):
    flag = True
    for tmp in t:
        if len(c) == len(tmp):
            f = True
            for i in range(len(c)):
                if c[i] != tmp[i] and tmp[i] != '*':
                    f = False
                    break
            if f:
                flag = False
            if not flag:
                break

    if not flag:
        s[g]='*'*len(c)
print(*s)