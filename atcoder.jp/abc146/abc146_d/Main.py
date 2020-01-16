import sys

sys.setrecursionlimit(100000)
n = int(input())
bfs_dic = [{} for i in range(n)]
ans = [0 for i in range(n-1)]

def bfs(pn, pc, node):
    c = 1
    max_c = 0
    
    if len(bfs_dic[node]) != 1 or pc == 0: #葉は見ない(葉でも最初だけは子を見る)
        for k,v in bfs_dic[node].items():
            if k == pn: continue #親と同じなら無視
            if pc == c:                 #親と色被っちゃったら色変え
                c+=1
            ans[v] = c
            maxable_c = bfs(node, c, k)
            if max_c < maxable_c:
                max_c = maxable_c
            c+=1                        #子と自分の間に色割り当てて色変える
        if max_c < c-1:
            return c-1
        else:
            return max_c
    return 1                                        #葉やったら1色しか使っとらん
            
for i in range(n-1):
    a,b = map(int, input().split())
    a-=1
    b-=1
    bfs_dic[a][b] = i
    bfs_dic[b][a] = i

print(bfs(-1, 0, 0))
for i in ans:
    print(i)