a = list(map(int, input().split()))
for i,num in enumerate(a):
    if num == 0:
        print(i+1)