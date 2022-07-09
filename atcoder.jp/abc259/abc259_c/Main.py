import sys
import random
import time

# from sys import stdin
# readline = stdin.readline
# sr=lambda: readline()
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    s=sr()
    t=sr()
    pre_s = ''
    t_i = 0
    s_i = 0
    pre_flg = False
    while s_i < len(s) and t_i < len(t):
        now_s = s[s_i]
        now_t = t[t_i]
        if now_s != now_t:
            if now_t == pre_s and pre_flg:
                while t_i < len(t) and t[t_i] == pre_s:
                    t_i+=1
                if t_i < len(t):
                    now_t = t[t_i]
                    if now_s != now_t:
                        print("No")
                        sys.exit()
                else:
                    print("No")
                    sys.exit()
            else:
                print("No")
                sys.exit()
        pre_flg = now_s == pre_s
        pre_s = now_s
        s_i+=1
        t_i+=1

    if s_i == len(s) and t_i < len(t):
        now_t=t[t_i]
        if now_t == pre_s and pre_flg:
            while t_i<len(t) and t[t_i]==pre_s:
                t_i+=1

    if t_i == len(t) and s_i == len(s):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
