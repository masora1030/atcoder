inf = 10 ** 18
mod = 10 ** 9 + 7

n = int(input())
s = [''.join(reversed(list(input()))) for i in range(n)]
s.sort()
for c in s:
    print(''.join(reversed(list(c))))