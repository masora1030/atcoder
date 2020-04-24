# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))

inf = 10**9+7
mod = 10**9+7
n, k = map(int, input().split())
g_val = [list(map(int, input().split())) for i in range(n)]
netalist = [False for i in range(n+1)]
netanum = [0 for i in range(n+1)]
g_val.sort(key=lambda x: x[1])
used_list = []
ans = [0 for i in range(k+1)] # i種類食べた時の最大値
preans = 0
for j in range(k):
    if g_val:
        g,v = g_val.pop()
        netalist[g] = True
        netanum[g]+=1
        used_list.append((v,g))
        preans+=v

kind = sum(list(map(int, netalist)))
ans[kind] = preans+(kind*kind)

import heapq # 優先度付きキュー(最小値取り出し)
heapq.heapify(used_list)   # ヒープ化


while used_list:
    v,g = heapq.heappop(used_list) # 最小値の取り出し
    if netanum[g] > 1:
        while g_val:
            gnew,vnew = g_val.pop()
            if netanum[gnew] == 0:
                ans[kind+1] = ans[kind]-v-(kind*kind)+vnew+((kind+1)*(kind+1))
                kind+=1
                netanum[g] -= 1
                netanum[gnew] += 1
                break
    if not g_val:
        break
print(max(ans))