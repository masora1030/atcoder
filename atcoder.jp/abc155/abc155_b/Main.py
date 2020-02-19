import sys
n = int(input())
a = list(map(int, input().split()))
for num in a:
    if (num % 2 == 0):
        if (num % 3 != 0 and num % 5 != 0):
            print('DENIED')
            sys.exit()
print('APPROVED')