# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
import sys
inf = 10**9+7
mod = 10**9+7
import bisect
n = int(input())
HS = [list(map(int, input().split())) for i in range(n)]


# min・・・実現不可・・・実現可能(最小)・・・実現可能・・・max となっている時用。
def judge(pre_ans):
    Time_limit = [0 for i in range(n)]
    for i in range(n):
        Time_limit[i] = (pre_ans - HS[i][0])//HS[i][1]
    Time_limit.sort()
    for i,time in enumerate(Time_limit):
        if i > time:
            return False  # 実現不可能
    return True


def bisect_judge(init_left=0, init_right=10**15):
    left = init_left
    right = init_right
    while left < right:
        mid = (left + right)//2
        if judge(mid): # Trueだったら実現可能
            right = mid
        else:          # Falseだったら実現不可能
            left = mid+1
    return right       # 実現可能なもので最小のもの

print(bisect_judge())