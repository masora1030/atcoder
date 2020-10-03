inf = 10 ** 18
mod = 10 ** 9 + 7

n = int(input())
a = list(map(int, input().split()))
def get2div(x):
    ret = 0
    while x%2 == 0:
        x //= 2
        ret += 1
    return ret
ans = inf
for num in a:
    ans = min(get2div(num), ans)
print(ans)