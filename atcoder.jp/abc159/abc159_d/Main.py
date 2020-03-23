n = int(input())
a = list(map(int, input().split()))
num_dic = {}
for i in a:
    if i in num_dic:
        num_dic[i]+=1
    else:
        num_dic[i] = 1
pre_ans = 0
for k,v in num_dic.items():
    pre_ans+=v*(v-1)//2
for num in a:
    tmp = num_dic[num]
    ans = pre_ans - (tmp-1)
    print(ans)