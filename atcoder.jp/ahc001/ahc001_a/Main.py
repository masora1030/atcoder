import bisect


from sys import stdin
readline = stdin.readline
sr = lambda: readline()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

inf = 10 ** 18
# mod = 10 ** 9 + 7
mod = 998244353
# len(bin(n)) - bin(n).rfind("1") - 1

def judge(a,b,c,d,visited,num):
    for i, abcd in enumerate(visited):
        aa, ab, ac, ad = abcd
        if i!=num and (d>ab and b<ad) and (c>aa and a<ac):
            return False
    return True

def getLimit(x,y,visited,num):
    bottom = 1
    top = 5000
    while top-bottom>1:
        mid = (top+bottom)//2
        flg = True
        tmp=mid//2
        if mid%2==1:
            flg = judge(x-tmp, y-tmp, x+tmp+1, y+tmp+1, visited, num)
        else:
            flg = judge(x-tmp, y-tmp, x+tmp, y+tmp, visited, num)
        if flg:
            bottom = mid
        else:
            top = mid
    return bottom

if __name__=='__main__':
    n = ir()
    h,w = 10000,10000
    xyr = [[lr(), [i]] for i in range(n)]
    visited=[[xxx[0],xxx[1],xxx[0]+1,xxx[1]+1] for xxx,_ in xyr]
    xyr.sort(key=lambda x:x[0][2])
    ans = [[xxx[0],xxx[1],xxx[0]+1,xxx[1]+1] for xxx,_ in xyr]
    kouho = [i*i for i in range(10000)]


    for xxx,I in xyr:
        x,y,r = xxx
        i = I[0]
        ind = bisect.bisect_left(kouho, r)
        if abs(kouho[ind-1]-r) <= abs(kouho[ind]-r):
            ind-=1

        limit_bounds = min(x+1, y+1, h-y, w-x)
        limit = min(getLimit(x,y,visited,i),limit_bounds)

        a,b,c,d = 0,0,0,0

        if limit<=ind:
            tmp = limit//2
            if limit%2==1:
                a,b,c,d = x-tmp,y-tmp,x+tmp+1,y+tmp+1
            else:
                a,b,c,d = x-tmp, y-tmp, x+tmp, y+tmp
        else:
            tmp = ind//2
            if ind%2==1:
                a, b, c, d=x-tmp, y-tmp, x+tmp+1, y+tmp+1
            else:
                a, b, c, d=x-tmp, y-tmp, x+tmp, y+tmp
        ans[i] = [a,b,c,d]
        visited[i] = [a,b,c,d]

    for a,b,c,d in ans:
        print(f"{a} {b} {c} {d}")
