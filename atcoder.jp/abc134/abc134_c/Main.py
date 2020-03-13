# C
n = int(input())
a = [int(input()) for i in range(n)]
maxa = [-1,0]
premaxa = [-1,-1]
for i,num in enumerate(a):
    if num >= maxa[1]:
        premaxa = [maxa[0], maxa[1]]
        maxa = [i,num]
    elif num > premaxa[1]:
        premaxa = [i,num]
for i in range(n):
    if i == maxa[0]:
        print(premaxa[1])
    else:
        print(maxa[1])