h = int(input())
total = 0
while h > 0:
    h = h//2
    total+=1
print(2**total - 1)