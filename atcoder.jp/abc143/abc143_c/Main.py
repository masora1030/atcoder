n = int(input())
s = input()
opt = ''
count = 0
for c in s:
    if c != opt:
        count+=1
        opt = c
print(count)