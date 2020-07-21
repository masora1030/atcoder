import bisect

n,k = map(int, input().split())
x = list(map(int, input().split()))
# 若さと順位の対応表
dic = {x[i]:(i+1) for i in range(n)}

# 候補者集合(若い順にソート)
judge = x[:k]
judge.sort()

# 上位k位まで
print(dic[judge[k-1]])

# 上位k+i位まで
for i in range(n-k):
    # k+i位の人を候補者に追加
    bisect.insort_left(judge, x[k+i])
    print(dic[judge[k-1]])