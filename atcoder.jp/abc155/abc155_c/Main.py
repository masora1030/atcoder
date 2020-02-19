n = int(input())
s_dic = {}
count = 0
for i in range(n):
    tmp = input()
    s_dic.setdefault(tmp, 0)
    s_dic[tmp] += 1
    if count < s_dic[tmp]:
        count = s_dic[tmp]
ans = [k for k, v in s_dic.items() if v == count]
ans.sort()
for a in ans:
    print(a)