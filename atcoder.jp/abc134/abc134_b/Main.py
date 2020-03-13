# B
n,d = map(int, input().split())
cansee = d*2 + 1
if n % cansee == 0:
    print(n//cansee)
else:
    print(n//cansee+1)