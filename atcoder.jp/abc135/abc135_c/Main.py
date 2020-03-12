n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
count = 0
for i, atc in enumerate(b):
    if a[i] >= atc:
        a[i] = a[i] - atc
        count+=atc
    else:
        atc = atc - a[i]
        count+=a[i]
        a[i] = 0
        if a[i+1] >= atc:
            a[i+1] = a[i+1] - atc
            count+=atc
        else:
            atc = atc - a[i+1]
            count+=a[i+1]
            a[i+1] = 0
print(count)