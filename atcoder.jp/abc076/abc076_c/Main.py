inf = 10**15
mod = 10**9+7
s = input()
t = input()
lenn = len(s)
lent = len(t)
ans = []
for i in range(lenn-lent+1):
    flag = True
    tmp = ['' for i in range(lenn)]
    for j,k in enumerate(range(i,i+lent)):
        if (s[k] != t[j]) and (s[k] != '?'):
            flag = False
            break
        else:
            tmp[k]=t[j]
    if flag:
        for l in range(lenn):
            if tmp[l] == '':
                if s[l] == '?':
                    tmp[l] = 'a'
                else:
                    tmp[l] = s[l]
        ans.append(''.join(tmp))
ans.sort()
if ans:
    print(ans[0])
else:
    print('UNRESTORABLE')