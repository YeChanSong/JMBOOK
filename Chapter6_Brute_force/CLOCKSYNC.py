import sys
sys.setrecursionlimit(100000000)
b = [(0,1,2),(3,7,9,11),(4,10,14,15),(0,4,5,6,7),(6,7,8,10,12),(0,2,14,15),(3,14,15),(4,5,7,14,15),(1,2,3,4,5),(3,4,5,9,13)]

def recur(combi, btn):
    '''
    combi: 현재의 버튼 누른 결과 리스트
    btn: 버튼 번호
    '''
    global b, ori
    ret = 9999
    if btn == 10:
        return 9999
    if ori == combi:
        return 0
    
    for i in range(4):
        ret = min(ret, i + recur(combi.copy(),btn+1))
        
        for j in b[btn]:
            combi[j] +=3
            if combi[j] > 12:
                combi[j] = 3
        
        
    return ret
    

C = int(input())
for i in range(C):
    global clock, ori
    ori = [12 for i in range(16)]
    clock = list(map(int,input().split()))
    
    answer = recur(clock,0)
    
    if answer == None:
        answer = -1
    print(answer)