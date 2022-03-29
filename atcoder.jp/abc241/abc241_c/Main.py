sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    n=ir()
    s=[sr() for _ in range(n)]
    flg = False
    for i in range(n-5):
        for j in range(n):
            tmp = 0
            for k in range(6):
                if s[i+k][j] == '#':
                    tmp+=1
            if tmp >= 4:
                flg = True
                break
            tmp=0
            for k in range(6):
                if s[j][i+k]=='#':
                    tmp+=1
            if tmp>=4:
                flg=True
                break
        if flg:
            break
    if not flg:
        for i in range(n-5):
            for j in range(n-5):
                tmp=0
                for k in range(6):
                    if s[i+k][j+k]=='#':
                        tmp+=1
                if tmp>=4:
                    flg=True
                    break
                tmp=0
                for k in range(6):
                    if s[i+k][j+5-k]=='#':
                        tmp+=1
                if tmp>=4:
                    flg=True
                    break
            if flg:
                break
    if flg:
        print("Yes")
    else:
        print("No")



if __name__ == '__main__':
    main()
