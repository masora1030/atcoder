import sys
k = int(input())
klist=list(map(str, [1,2,3,4,5,6,7,8,9]))
dic = {'0':['0','1'], '1':['0','1','2'], '2':['1','2','3'], '3':['2','3','4'], '4':['3','4','5'], '5':['4','5','6'], '6':['5','6','7'], '7':['6','7','8'], '8':['7','8','9'], '9':['8','9']}
if k <= 9:
    print(klist[k-1])
    sys.exit()
else:
    count = 0
    ok = 9
    while 1:
        tmp = klist[count]
        for add in dic[tmp[-1]]:
            klist.append(''.join([tmp, add]))
            ok+=1
            if ok == k:
                print(''.join([tmp, add]))
                sys.exit()
        count+=1