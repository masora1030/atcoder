inf = 10**15
mod = 10**9+7
def getans(x,y):
    count=1
    while 2*x <= y:
        x *= 2
        count+=1
    return count

x,y = map(int, input().split())
print(getans(x,y))