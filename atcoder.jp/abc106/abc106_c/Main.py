inf = 10 ** 15
mod = 10 ** 9 + 7

s = input()
k = int(input())
count1 = 0
other = ''
for c in s:
    if c == '1':
        count1+=1
    else:
        other = c
        break
if other == '':
    print(1)
else:
    if k <= count1:
        print(1)
    else:
        print(other)