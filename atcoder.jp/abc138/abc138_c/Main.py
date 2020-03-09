# C
import heapq # 優先度付きキュー(最小値取り出し)
n = int(input())
v = list(map(int, input().split()))
heapq.heapify(v)   # ヒープ化
ans = 0
for i in range(n-1):
    tmp1 = heapq.heappop(v)               # 最小値の取り出し
    tmp2 = heapq.heappop(v)               # 最小値の取り出し
    tmp = (tmp1 + tmp2) / 2
    heapq.heappush(v, tmp)
ans = heapq.heappop(v)               # 最小値の取り出し
print(ans)