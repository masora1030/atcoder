inf = 10 ** 15
mod = 10 ** 9 + 7
h,w = map(int, input().split())
maps = [input() for i in range(h)]
remh = []
remw = []
for i in range(h):
    flag = True
    for j in range(w):
        if maps[i][j] == '#':
            flag = False
            break
    if not flag:
        remh.append(i)
for j in range(w):
    flag = True
    for i in range(h):
        if maps[i][j] == '#':
            flag = False
    if not flag:
        remw.append(j)

for num in remh:
    a = []
    for tmp in remw:
        a.append(maps[num][tmp])
    s = ''.join(a)
    print(s)
