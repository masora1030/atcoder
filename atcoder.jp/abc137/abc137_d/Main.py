import heapq # 優先度付きキュー(最小値取り出し)

inf = 10**15
mod = 10**9+7
n,m = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n)]
ab.sort(key = lambda x:x[0], reverse = True)
q = []
heapq.heapify(q)   # ヒープ化
ans = 0
for i in range(1,m+1): # m-i日目からスタートして間に合う仕事
    while ab and ab[-1][0] == i:
        _,val = ab.pop()
        heapq.heappush(q, (-1) * val)
    if q:
        ans += heapq.heappop(q) * (-1)

print(ans)