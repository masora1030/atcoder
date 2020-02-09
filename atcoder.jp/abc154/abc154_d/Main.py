n,k = map(int, input().split())
dice = list(map(int, input().split()))
dice_sum = [0]
for i in dice:dice_sum.append(dice_sum[-1]+(i+1)/2)
def SumArea(r, l):
    return dice_sum[l]-dice_sum[r]

ans = 0
for i in range(n-k+1):
    tmp = SumArea(i, i+k)
    if tmp >= ans:
        ans = tmp
print(ans)