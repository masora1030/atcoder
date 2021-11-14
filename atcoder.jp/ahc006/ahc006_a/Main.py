import time
import random
import itertools
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

# import numpy as np

if __name__=='__main__':
    start_time=time.perf_counter()
    pre_time = 1.5
    P=14
    K=6
    m = 50
    n = 1000
    goals = []
    starts = []
    start_x_inds = {}
    for i in range(1000):
        a,b,c,d = lr()
        starts.append([a,b])
        goals.append([c,d])
    need_goals = [] # ind を append
    count = 0
    n_x, n_y = 400, 400
    start_visited = [False for i in range(n)]
    goal_visited = [False for i in range(n)]
    ans_r = []
    ans_xy = [400, 400]
    while count < m:
        # 現在地から最も距離が近いところから。
        goal_min_d = inf
        start_min_d = inf
        goal_ind = -1
        start_ind = -1
        if need_goals:
            for ind in need_goals:
                if goal_visited[ind] == False:
                    g_x,g_y = goals[ind]
                    dist = abs(n_x-g_x)+abs(n_y-g_y)
                    if goal_min_d > dist:
                        goal_min_d = dist
                        goal_ind = ind
        for ind in range(n):
            if start_visited[ind] == False:
                s_x, s_y = starts[ind]
                dist = abs(n_x-s_x)+abs(n_y-s_y)
                if start_min_d > dist:
                    start_min_d = dist
                    start_ind = ind
        if goal_min_d < start_min_d:
            goal_visited[goal_ind] = True
            g_x,g_y = goals[goal_ind]
            start_x_inds[len(ans_xy)] = False
            ans_xy.append(g_x)
            ans_xy.append(g_y)
            n_x, n_y = g_x, g_y
        else:
            start_visited[start_ind] = True
            s_x, s_y = starts[start_ind]
            start_x_inds[len(ans_xy)] = True
            ans_xy.append(s_x)
            ans_xy.append(s_y)
            ans_r.append(start_ind+1)
            need_goals.append(start_ind)
            n_x, n_y = s_x, s_y
            count+=1

    # 渡し切れてないところを渡す
    kitaku = False
    while not kitaku:
        # 現在地から最も距離が近いところから。
        goal_min_d=inf
        goal_ind=-1
        if need_goals:
            for ind in need_goals:
                if goal_visited[ind] == False:
                    g_x,g_y = goals[ind]
                    dist = abs(n_x-g_x)+abs(n_y-g_y)
                    if goal_min_d > dist:
                        goal_min_d = dist
                        goal_ind = ind
        if goal_ind != -1:
            goal_visited[goal_ind]=True
            g_x, g_y = goals[goal_ind]
            start_x_inds[len(ans_xy)] = False
            ans_xy.append(g_x)
            ans_xy.append(g_y)
            n_x, n_y = g_x, g_y
        else:
            kitaku = True
    ans_xy.append(400)
    ans_xy.append(400)

    def judge_score(ans):
        x,y = ans[0], ans[1]
        N = len(ans)//2
        ret = 0
        for i in range(N):
            nt_x, nt_y = ans[i*2], ans[i*2+1]
            ret+=abs(nt_x-x)+abs(nt_y-y)
            x=nt_x
            y=nt_y
        return ret

    def get_p_1(p):
        dice=list(range(0, 2))
        w = [p, 1]
        return random.choices(dice, k=1, weights=w)[0]

    scores = judge_score(ans_xy)
    # print(f"init score : {scores}")

    ######
    # 時間いっぱい色々パターン探索する。
    p=P
    while True:
        end_time=time.perf_counter()
        elapsed_time=end_time-start_time
        if elapsed_time>pre_time:
            break
        need_goals=[]  # ind を append
        count=0
        n_x, n_y=400, 400
        start_visited=[False for i in range(n)]
        goal_visited=[False for i in range(n)]
        pre_ans_r=[]
        pre_ans_xy=[400, 400]
        while count<m:
            # 現在地から最も距離が近いところから。たまに２番目に近いものを採用
            goal_min_d=inf
            goal_min_d2=inf
            start_min_d=inf
            start_min_d2=inf
            goal_ind=-1
            goal_ind2=-1
            start_ind=-1
            start_ind2=-1
            if need_goals:
                for ind in need_goals:
                    if goal_visited[ind]==False:
                        g_x, g_y=goals[ind]
                        dist=abs(n_x-g_x)+abs(n_y-g_y)
                        if goal_min_d>dist:
                            goal_min_d2=goal_min_d
                            goal_ind2=goal_ind
                            goal_min_d=dist
                            goal_ind=ind
                        elif goal_min_d2>dist:
                            goal_min_d2=dist
                            goal_ind2=ind

            for ind in range(n):
                if start_visited[ind]==False:
                    s_x, s_y=starts[ind]
                    dist=abs(n_x-s_x)+abs(n_y-s_y)
                    if start_min_d>dist:
                        start_min_d2=start_min_d
                        start_ind2=start_ind
                        start_min_d=dist
                        start_ind=ind
                    elif start_min_d2>dist:
                        start_min_d2=dist
                        start_ind2=ind

            if goal_min_d<start_min_d:
                # p 回に 1 回 1 が帰ってくる。
                if get_p_1(p)==1 and goal_ind2!=-1:
                    goal_ind=goal_ind2
                goal_visited[goal_ind]=True
                g_x, g_y=goals[goal_ind]
                pre_ans_xy.append(g_x)
                pre_ans_xy.append(g_y)
                n_x, n_y=g_x, g_y
            else:
                # p 回に 1 回 1 が帰ってくる。
                if get_p_1(p)==1:
                    start_ind=start_ind2
                start_visited[start_ind]=True
                s_x, s_y=starts[start_ind]
                pre_ans_xy.append(s_x)
                pre_ans_xy.append(s_y)
                pre_ans_r.append(start_ind+1)
                need_goals.append(start_ind)
                n_x, n_y=s_x, s_y
                count+=1

        # 渡し切れてないところを渡す
        kitaku=False
        while not kitaku:
            # 現在地から最も距離が近いところから。
            goal_min_d=inf
            goal_min_d2=inf
            goal_ind=-1
            goal_ind2=-1
            if need_goals:
                for ind in need_goals:
                    if goal_visited[ind]==False:
                        g_x, g_y=goals[ind]
                        dist=abs(n_x-g_x)+abs(n_y-g_y)
                        if goal_min_d>dist:
                            goal_min_d2=goal_min_d
                            goal_ind2=goal_ind
                            goal_min_d=dist
                            goal_ind=ind
                        elif goal_min_d2>dist:
                            goal_min_d2=dist
                            goal_ind2=ind
            if goal_ind!=-1:
                # p 回に 1 回 1 が帰ってくる。
                if get_p_1(p)==1 and goal_ind2!=-1:
                    goal_ind=goal_ind2
                goal_visited[goal_ind]=True
                g_x, g_y=goals[goal_ind]
                pre_ans_xy.append(g_x)
                pre_ans_xy.append(g_y)
                n_x, n_y=g_x, g_y
            else:
                kitaku=True
        pre_ans_xy.append(400)
        pre_ans_xy.append(400)

        pre_score=judge_score(pre_ans_xy)
        if pre_score<scores:
            scores=pre_score
            ans_xy=pre_ans_xy.copy()
            ans_r=pre_ans_r.copy()

    # print(f"pre score : {scores}")

    ######
    # デフォルトのをいじる方向
    # 時間いっぱい色々パターン探索する。
    k=K
    while True:
        end_time=time.perf_counter()
        elapsed_time=end_time-start_time
        if elapsed_time > 1.8:
            break
        # 連続するk点をとって来て、中k-2点をswapし、現状よりよかったら採択というのを繰り返す
        # 点は、総合で102個ある。index = [1,2,...,k],  [2,3,...,k+1], ... , [101-k+1,...,100,101]
        # [swap_ind*2+2, swap_ind*2+3] と [swap_ind*2+4, swap_ind*2+5] を swap して
        # 差分を評価
        swap_ind = random.randint(1, 101-k+1)
        # 出発/到着が一致していなければスルー
        flg = False
        pre = start_x_inds[swap_ind*2+2]
        for i in range(k-2):
            if pre != start_x_inds[swap_ind*2+2+2*i]:
                flg = True
                break
        if flg:
            continue

        swap_xs = [ans_xy[swap_ind*2+2*i] for i in range(k)]
        swap_ys = [ans_xy[swap_ind*2+2*i+1] for i in range(k)]

        min_dist = inf
        min_dist_li = tuple([j+1 for j in range(k-2)])

        for li in list(itertools.permutations([j+1 for j in range(k-2)])):
            pre_dist = 0
            x,y = swap_xs[0], swap_ys[0]
            for ind in li:
                ne_x,ne_y = swap_xs[ind],swap_ys[ind]
                pre_dist += abs(ne_x-x)+abs(ne_y-y)
                x,y = ne_x,ne_y
            pre_dist+=abs(swap_xs[-1]-x)+abs(swap_ys[-1]-y)
            if min_dist > pre_dist:
                min_dist = pre_dist
                min_dist_li = li

        for j in range(k-2):
            ans_xy[swap_ind*2+2+2*j] = swap_xs[min_dist_li[j]]
            ans_xy[swap_ind*2+2+2*j+1] = swap_ys[min_dist_li[j]]
    ######

    scores = judge_score(ans_xy)
    # print(f"best score : {scores}")
    print(f"{m} {' '.join([str(num) for num in ans_r])}")
    print(f"{len(ans_xy)//2} {' '.join([str(num) for num in ans_xy])}")
