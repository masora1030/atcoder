# B
def keta(n):
    count = 0
    while n != 0:
        n = n//10
        count+=1
    return count

n  = int(input())
k = keta(n)
if k == 1:
    print(n)
elif k == 2:
    print(9)
elif k == 3:
    print(9 + n-99)
elif k == 4:
    print(909)
elif k == 5:
    print(909 + n-9999)
elif k == 6:
    print(90909)
    