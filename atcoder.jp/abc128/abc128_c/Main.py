n,m = map(int, input().split())
dic_s = {}
for i  in range(n):
    dic_s[i] = []
for i in range(m):
    a = list(map(int, input().split()[1:]))
    for num in a:
        dic_s[num-1].append(i)
p = list(map(int, input().split()))
total = 0

def judge_bright(judge):
    for i,num in enumerate(judge):
        if num%2 != p[i]:
            return False
    return True

for i in range(2 ** n): # n個のスイッチの組み合わせ
    judge = [0 for i in range(m)]
    for j in range(n):  # このループが一番のポイント
        if ((i >> j) & 1):  # 1だったら(オンだったら)
            for d in dic_s[j]: #jのスイッチにつながる電球がカウントされる
                judge[d] += 1
    
    if judge_bright(judge):      # ぜんぶついた！
        total+=1
print(total)