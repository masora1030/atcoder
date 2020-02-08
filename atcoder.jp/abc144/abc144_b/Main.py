n = int(input())
judge = []
for i in range(9):
    for j in range(9):
        judge.append((i+1)*(j+1))
if n in judge:
    print('Yes')
else:
    print('No')