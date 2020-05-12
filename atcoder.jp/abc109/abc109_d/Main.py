inf = 10 ** 15
mod = 10 ** 9 + 7
h,w = map(int, input().split())
a = [list(map(int, input().split())) for i in range(h)]
ans = []
for i in range(h):
    if i%2 == 0:
        for j in range(w-1):
            if a[i][j] != 0:
                if a[i][j]%2 == 1:    # 奇数だった
                    ans.append([i,j,i,j+1])
                    a[i][j]-=1
                    a[i][j+1]+=1
        if i < h-1 and a[i][w-1]%2 == 1:
            ans.append([i, w-1, i+1, w-1])
            a[i][w-1]-=1
            a[i+1][w-1]+=1
    else:
        for j in range(w-1):
            if a[i][w-1-j]%2 == 1:
                ans.append([i,w-1-j,i,w-1-j-1])
                a[i][w-1-j]-=1
                a[i][w-1-j-1]+=1
        if i < h-1 and a[i][0]%2 == 1:
            ans.append([i,0,i+1,0])
            a[i][0]-=1
            a[i+1][0]+=1
print(len(ans))
for x,y,nx,ny in ans:
    print('{} {} {} {}'.format(x+1,y+1,nx+1,ny+1))