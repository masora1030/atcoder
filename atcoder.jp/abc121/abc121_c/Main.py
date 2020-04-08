n,m = map(int, input().split())
Drink = [[] for i in range(n)]
for i in range(n):
    Drink[i] = list(map(int, input().split()))
# 値段安い店順にソート
Drink.sort(key=lambda x: x[0])
ans = 0 # 値段
count = 0 # 総数
ind = 0 # 回る店
while count < m:
    p,num = Drink[ind] # 価格と数
    if count+num < m:
        count+=num
        ans+=p*num
        ind+=1
        continue
    else:
        ans+=p*(m-count)
        count=m
print(ans)