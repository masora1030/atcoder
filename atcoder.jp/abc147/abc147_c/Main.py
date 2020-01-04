n = int(input())
a = [[-1 for i in range(n)] for j in range(n)]
x = 0
max = 0
flag = 0
for i in range(n):
    x = int(input())
    for j in range(x):
        y,z = map(int, input().split())
        a[i][y-1] = z
for i in range(2**n):
    flag = 0
    for j in range(n):
        if (i >> j) & 1 == 1:
            for k in range(n):
                if a[j][k] != -1:
                    if a[j][k] != (i >> k) & 1:
                        flag = 1
                        break
            if flag == 1:
                break
    if flag == 1:
        continue
    elif j == n-1:
        count = 0
        for j in range(n):
            if (i >> j) & 1 == 1:
                count+=1
        if count > max:
            max = count
print(max)