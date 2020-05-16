inf = 10 ** 15
mod = 10 ** 9 + 7

d,g = map(int, input().split())
p = [list(map(int, input().split())) for i in range(d)]
p.reverse()
ans = inf
for i in range(2**d):
    count = 0
    total = 0
    for j in range(d):  # このループが一番のポイント
        if ((i >> j) & 1):  # 1だったら(オンだったら)
            count += p[j][0]
            total += p[j][0] * 100*(d-j) + p[j][1]
    if total >= g:
        ans = min(ans, count)
    else:
        for j in range(d):
            if not ((i >> j) & 1):
                num = p[j][0]
                score = 100*(d-j)
                if score*num >= g-total:
                    must = (g-total+score-1)//score
                    total+=score*must
                    count+=must
                    break
                else:
                    total+=score*num
                    count+=num
        ans = min(ans, count)
print(ans)