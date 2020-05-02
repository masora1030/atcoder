k = int(input())
tmp = 100
count = 0
while tmp < k:
    tmp = int(tmp*1.01)
    count+=1
print(count)