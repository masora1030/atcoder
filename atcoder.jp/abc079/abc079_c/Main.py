import sys
inf = 10**15
mod = 10**9+7
s = input()
n = len(s)-1
for i in range(2**n):
    ans = int(s[0])
    acc = ans
    a = [s[0]]
    for j in range(n):
        if ((i >> j) & 1):  # 1だったら(オンだったら)
            acc = int(s[j + 1])
            ans+=acc
            a.append('+')
            a.append(s[j+1])
        else:
            acc = int(s[j + 1])
            ans-=acc
            a.append('-')
            a.append(s[j+1])
    if ans == 7:
        a.append('=7')
        print(''.join(a))
        sys.exit()