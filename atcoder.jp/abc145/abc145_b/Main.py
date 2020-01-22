import sys
n = int(input())
s = input()
if n%2 == 0:
    for i in range(n//2):
        if s[i] != s[i+(n//2)]:
            print('No')
            sys.exit(0)
    print('Yes')
else:
    print('No')