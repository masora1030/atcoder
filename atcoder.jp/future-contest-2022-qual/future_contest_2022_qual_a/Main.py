import sys
import bisect
from collections import deque
import itertools
import math
import heapq
import random

# import sys
# sys.setrecursionlimit(10**6)
from sys import stdin
# readline = stdin.readline
# sr=lambda: readline()

import random
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

import numpy as np

if __name__=='__main__':

    # Prior information
    n, m, k, r=list(map(int, input().split()))
    task_difficulty=[]
    for i in range(n):
        task_difficulty.append(list(map(int, input().split())))
    task_sum_index_tuple = [(sum(li),ind) for ind,li in enumerate(task_difficulty)]

    task_dependency=[[] for _ in range(n)]
    task_root=[[] for _ in range(n)]
    for i in range(r):
        temp=list(map(int, input().split()))
        task_dependency[temp[0]-1].append(temp[1]-1)
        task_root[temp[1]-1].append(temp[0]-1)

    task_status = [-1 for _ in range(n)]
    # -1 : not ready
    # 0 : in ready task list
    # 1 : running
    # 2 : done

    member_status = [[-1,-1,0] for _ in range(m)]
    # (-1,-1,num) : not working. done num jobs.
    # (t,d,num) : working at task t in d days. done num jobs.

    member_ability = [[0 for _ in range(k)] for _ in range(m)]


    # 用意できているtask
    ready_task = []
    for ind,li in enumerate(task_difficulty):
        if len(task_root[ind]) == 0:
            heapq.heappush(ready_task, task_sum_index_tuple[ind])
            task_status[ind] = 0

    wait_member_num = m

    def init_member_ability():
        for member_ind in range(m):
            pre_s = np.abs(np.random.normal(loc=0,scale=1,size=k)).tolist()
            l2norm = 0
            for num in pre_s:
                l2norm+=num*num
            l2norm = l2norm**(1/2)
            pre_q = np.random.uniform(20,60,k).tolist()
            for skill_ind in range(k):
                member_ability[member_ind][skill_ind] = int(pre_s[skill_ind]*pre_q[skill_ind]/l2norm)
            print(f"#s {member_ind+1} {' '.join([str(num) for num in member_ability[member_ind]])}")

    def judge_member(task_ind):
        task_dif = task_difficulty[task_ind]
        ret_ind = -1
        now_score = inf # 低い方がいい
        for member_ind in range(m):
            status = member_status[member_ind]
            if status[0] != -1:
                continue
            score = 0
            for skill_ind, skill_num in enumerate(member_ability[member_ind]):
                task_skill_num = task_dif[skill_ind]
                score += max(task_skill_num-skill_num, 0)
            if score == 0:
                score = 1
            else:
                score = max(1, score)
            if score < now_score:
                ret_ind = member_ind
                now_score = score
        return ret_ind

    def update_member_working_day():
        for member_ind in range(m):
            status = member_status[member_ind]
            if status[0] == -1:
                continue
            member_status[member_ind][1]+=1

    def update_member_ability(done_member, done_task, day):
        status = member_status[done_member]
        task_dif = task_difficulty[done_task]
        done_work_num = status[2]
        real_work_days = status[1]
        predict_work_days=0
        for skill_ind, skill_num in enumerate(member_ability[done_member]):
            task_skill_num=task_dif[skill_ind]
            predict_work_days+=max(task_skill_num-skill_num, 0)
        if predict_work_days==0:
            predict_work_days=1
        else:
            predict_work_days=max(1, predict_work_days)
        gap = real_work_days-predict_work_days

        if gap == 0:
            pass
        elif gap > 0:
            # 予測能力を下げる方向に。gap の絶対値が大きいほど下げた方がいい。
            # 各 skill について d-s が小さいほど（間違えている可能性があるので）下げた方がいい。が、一旦一律で下げる
            # 合計でgapだけ下げるようにする。
            # 基準は、gap // k とかで良さそう。
            valid_num=0
            for skill_ind, skill_num in enumerate(member_ability[done_member]):
                if member_ability[done_member][skill_ind]-(gap//k) >= 0:
                    valid_num+=1
            for skill_ind, skill_num in enumerate(member_ability[done_member]):
                member_ability[done_member][skill_ind]-=(gap//valid_num)
                if member_ability[done_member][skill_ind] < 0:
                    member_ability[done_member][skill_ind]+=(gap//valid_num)
            print(f"#s {done_member+1} {' '.join([str(num) for num in member_ability[done_member]])}")
        else:
            # 予測能力を上げる方向に。gap の絶対値が大きいほど上げた方がいい。
            # 各 skill について d-s が大きいほど（間違えている可能性があるので）上げた方がいい。
            # 合計でgapだけ上げるようにする。
            # 基準は、gap // k とかで良さそう。
            gap = abs(gap)
            valid_num = 0
            for skill_ind, skill_num in enumerate(member_ability[done_member]):
                if member_ability[done_member][skill_ind]+(gap//k) <= 40:
                    valid_num+=1
            for skill_ind, skill_num in enumerate(member_ability[done_member]):
                member_ability[done_member][skill_ind]+=(gap//valid_num)
                if member_ability[done_member][skill_ind] > 40:
                    member_ability[done_member][skill_ind]-=(gap//valid_num)
            print(f"#s {done_member+1} {' '.join([str(num) for num in member_ability[done_member]])}")

    init_member_ability()
    day = 0
    while True:
        output=[0]
        # job を投げる
        while wait_member_num > 0 and len(ready_task) > 0:
            task = heapq.heappop(ready_task)
            task_ind = task[1]

            # task に沿ってかつ稼働できる member を task に割り当てる。
            member_ind = judge_member(task_ind)

            output[0]+=1
            output.append(member_ind+1)
            output.append(task_ind+1)

            # task 開始したら、
            # 1. タスクのステータスの更新
            task_status[task_ind]=1
            # 2. メンバーステータスの更新
            member_status[member_ind][0] = task_ind
            member_status[member_ind][1] = 0 # 毎日更新される必要あり
            # 3. wait_member_numの更新
            wait_member_num-=1

        str_output=map(str, output)
        print(" ".join(str_output))
        # After the output, you have to flush Standard Output
        sys.stdout.flush()

        day+=1
        # member_status[member_ind][1] 更新
        update_member_working_day()
        # day 日目の job 状態を受け取る
        tmp=list(map(int, input().split()))
        if len(tmp)==1:
            if tmp[0]==-1:
                break
            else:
                pass
        else:
            for done_member in tmp[1:]:
                done_member-=1
                done_task = member_status[done_member][0]
                # 1. タスクステータスの更新
                task_status[done_task]=2
                # 2. ready_taskの更新 (push)
                for next_task in task_dependency[done_task]:
                    assert task_status[next_task]==-1
                    add_flg = True
                    for root_task in task_root[next_task]:
                        if task_status[root_task] < 2:
                            add_flg = False
                            break
                    if add_flg:
                        heapq.heappush(ready_task, task_sum_index_tuple[next_task])
                        task_status[next_task]=0

                # 3. メンバー能力の更新
                update_member_ability(done_member, done_task, day)

                # 4. メンバーステータスの更新
                member_status[done_member][0]=-1
                member_status[done_member][1]=-1
                member_status[done_member][2]+=1

                # 5. wait_member_numの更新
                wait_member_num+=1
