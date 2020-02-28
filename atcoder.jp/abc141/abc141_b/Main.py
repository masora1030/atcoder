import sys
s = input()
for i, notes in enumerate(s):
    if i%2 == 1:
        if notes == 'R':
            print('No')
            sys.exit()
    else:
        if notes == 'L':
            print('No')
            sys.exit()
print('Yes')