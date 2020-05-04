import sys
import bisect
inf = 10**15
mod = 10**9+7
ans = []
n,a,b,c = map(int, input().split())
abc = []


for i in range(n):
    s = input()
    abc.append(s)

for i in range(n):
    s = abc[i]
    if s == 'AB':
        if a > b:
            a-=1
            b+=1
            ans.append('B')
        elif a < b:
            a+=1
            b-=1
            ans.append('A')
        else:
            if i != n-1 and abc[i+1] == 'AC':
                a += 1
                b -= 1
                ans.append('A')
            else:
                a -= 1
                b += 1
                ans.append('B')
    elif s == 'BC':
        if b > c:
            b-=1
            c+=1
            ans.append('C')
        elif b < c:
            b+=1
            c-=1
            ans.append('B')
        else:
            if i != n-1 and abc[i + 1] == 'AB':
                b += 1
                c -= 1
                ans.append('B')
            else:
                b -= 1
                c += 1
                ans.append('C')
    else:
        if c > a:
            c-=1
            a+=1
            ans.append('A')
        elif c < a:
            c+=1
            a-=1
            ans.append('C')
        else:
            if i != n-1 and abc[i + 1] == 'BC':
                c += 1
                a -= 1
                ans.append('C')
            else:
                c -= 1
                a += 1
                ans.append('A')
    if a < 0 or b < 0 or c < 0:
        print('No')
        sys.exit()
if a >= 0 and b >= 0 and c >= 0:
    print('Yes')
    for num in ans:
        print(num)
else:
    print('No')