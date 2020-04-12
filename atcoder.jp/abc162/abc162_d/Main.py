import bisect

n = int(input())
s = input()
r = []
b = []
g = []
for i,c in enumerate(s):
    if c == 'R':
        r.append(i)
    elif c == 'B':
        b.append(i)
    else:
        g.append(i)
g_leng = len(g)
r_leng = len(r)
b_leng = len(b)
ans = g_leng*r_leng*b_leng
subans = 0
for j in b:
    for i in r:
        g_ind = bisect.bisect_left(g, 2*j-i)
        if g_ind != g_leng and g[g_ind] == 2*j-i:
            subans+=1
        g_ind = bisect.bisect_left(g, 2*i-j)
        if g_ind != g_leng and g[g_ind] == 2*i-j:
            subans+=1
        g_ind = bisect.bisect_left(g, (i + j) // 2)
        if g_ind != g_leng and g[g_ind] == (i + j) / 2:
            subans += 1
print(ans-subans)