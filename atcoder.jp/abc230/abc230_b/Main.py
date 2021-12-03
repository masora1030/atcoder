sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# mod = 10**9+7
mod = 998244353

if __name__=='__main__':
    s=sr()
    tmp = ["o", "x", "x"]
    kouho=[]
    for i in range(3):
        pre=[]
        for j in range(len(s)):
            pre.append(tmp[(i+j)%3])
        kouho.append("".join(pre))
    flg=False
    for ko in kouho:
        if s==ko:
            flg=True
            break
    if flg:
        print("Yes")
    else:
        print("No")