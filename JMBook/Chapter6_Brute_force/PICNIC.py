import sys
sys.setrecursionlimit(1000000)
from copy import deepcopy

def recur(friend,set):
    '''
    friend: 남은 친구 관계를 나타내는 튜플 리스트
    set: 친구 관계가 정해져야 할 학생들
    반환되는 값은 가능한 조합의 수
    '''
    total = 0
    if len(set) == 0:
        return 1
    # 학생들이 모두 분류된 경우 종료
    tmpfriend = deepcopy(friend)
    for i  in friend:
        if i[0] in set and i[1] in set:
            tmp = deepcopy(set)
            tmp.remove(i[0])
            tmp.remove(i[1])
            #tmpfriend.remove(i)
            #print(tmpfriend)
            total += recur(tmpfriend,tmp)
        tmpfriend.remove(i)
    return total

C = int(input())

for i in range(C):
    n, m = map(int,input().split())
    tmp = list(input().split())
    friend = [(int(tmp[i*2]),int(tmp[i*2 +1])) for i in range(len(tmp)//2) ]
    # 각 테스트케이스 입력 처리
    #ret = recur(friend,[i for i in range(n)])
    print(recur(friend,list(range(n))))

