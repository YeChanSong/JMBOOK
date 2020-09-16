import sys
sys.setrecursionlimit(1000000)

def recur(set,num):
    '''
    set: 지정된 친구들
    num: 짝을 지정할 친구
    '''
    total = 0
    global n, friend
    if num >= n:
        return 0
    if len(set) == n:
        return 1
    if num in set:
        return recur(set,num+1)
    
    for i in range(num+1,n):
        flag = False
        if i not in set:
            for j in range(len(friend)//2):
                
                if (friend[j*2] == num and friend[j*2+1] == i)\
                    or (friend[j*2] == i and friend[j*2+1] == num):
                        if flag == False:
                            tmp = set.copy()
                            tmp.append(num)
                            tmp.append(i)
                            #print(tmp)
                            total += recur(tmp,num+1)
                            flag = True
        else:
            total += recur(set,num+1)
            
    return total
    
    

C = int(input())

for i in range(C):
    global n, m
    n, m = map(int,input().split())
    global friend
    friend = list(map(int,input().split()))
    empty = []
    print(recur(empty,0))

