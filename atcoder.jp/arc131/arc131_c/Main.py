sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# mod = 10**9+7
mod = 998244353

if __name__=='__main__':
    n=ir()
    a=lr()
    dic={}
    dic1={}
    init = 0
    for num in a:
        if num in dic:
            dic[num]+=1
        else:
            dic[num]=1
        init = init ^ num
    tmp_init = 0
    for num in a:
        tmp = init ^ num
        tmp_init = tmp_init ^ tmp
        if tmp in dic1:
            dic1[tmp]+=1
        else:
            dic1[tmp]=1
    if 0 in dic1:
        print("Win")
    else:
        if init == tmp_init:
            print("Lose")
        else:
            print("Win")