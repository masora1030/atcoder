import heapq # 優先度付きキュー(最小値取り出し)
n,m = map(int, input().split())
a = list(map(int, input().split()))
a = list(map(lambda x: x*(-1), a))  # 各要素を-1倍

heapq.heapify(a)
for i in range(m):
    tmp = heapq.heappop(a)*(-1)   # 最大値の取り出し
    heapq.heappush(a, (-1)*(tmp//2)) # 1/2倍して最大値更新
print(-sum(a))