inf = 10 ** 15
mod = 10 ** 9 + 7
k = int(input())
s = input()
if len(s) <= k:
    print(s)
else:
    print('{}{}'.format(s[:k],'...'))