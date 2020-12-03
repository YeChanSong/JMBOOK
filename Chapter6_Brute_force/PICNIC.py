import sys
sys.setrecursionlimit(1000000)

def recur(freefriend):
    '''
    freefriend: 짝 결정 여부
    '''
    total = 0
    global n,m,friends
    findfriend = -1
    for i in range(len(freefriend)):
        if freefriend[i] == False:
            findfriend = i
            break
    
    if findfriend == -1:
        return 1
    mate = findfriend +1
    while mate < n:
        if freefriend[mate] == True:
            mate +=1
            continue
        else:
            if mate in friends[findfriend]:
                freefriend[mate] = True
                freefriend[findfriend] = True
                total += recur(freefriend)
                freefriend[mate] = False
                freefriend[findfriend] = False
        mate +=1
            
    
    return total
    

C = int(input())

for i in range(C):
    global n, m
    n, m = map(int,input().split())
    global friends
    
    freefriend = list(False for i in range(n))
    friends = []
    
    friend = list(map(int,input().split()))
    for k in range(n):
        tmp = []
        friends.append(tmp)
    for i in range(len(friend)//2):
        a, b = friend[i*2], friend[i*2 +1]
        if a > b:
            a, b = b, a
            friends[a].append(b)
        else:
            friends[a].append(b)
                
    print(recur(freefriend))
