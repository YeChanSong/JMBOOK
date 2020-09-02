import sys
sys.setrecursionlimit(100000)

def recur(board, start, tofind):
    '''
    board : 해당 테스트케이스의 게임판
    start : 현재 위치 튜플
    tofind : 남은 글자
    '''
    y, x = start
    if y < 0 or y > 4 or x < 0 or x > 4:
        return None
    # x,y 범위를 벗어난 경우 종료
    if len(tofind) == 0:
        return 'YES'
    
    if tofind[0] == board[y][x]:
        a = recur(board,(y-1,x-1),tofind[1:])
        if a == 'YES':
            return 'YES'
        b = recur(board,(y-1,x),tofind[1:])
        if b == 'YES':
            return 'YES'
        c = recur(board,(y-1,x+1),tofind[1:])
        if c == 'YES':
            return 'YES'
        d = recur(board,(y,x-1),tofind[1:])
        if d == 'YES':
            return 'YES'
        e = recur(board,(y,x+1),tofind[1:])
        if e == 'YES':
            return 'YES'
        f = recur(board,(y+1,x-1),tofind[1:])
        if f == 'YES':
            return 'YES'
        g = recur(board,(y+1,x),tofind[1:])
        if g == 'YES':
            return 'YES'
        h = recur(board,(y+1,x+1),tofind[1:])
        if h == 'YES':
            return 'YES'
        
        else:
            return 'NO'

    
C = int(input())
Board = []
Words = []
Nlist = []
for i in range(C):
    tmplist = []
    for j in range(5):
        tmp = input()
        tmplist.append(tmp)
    Board.append(tmplist)
    N = int(input())
    Nlist.append(N)
    tmplist = []
    for k in range(N):
        tmp = input()
        tmplist.append(tmp)
    Words.append(tmplist)


# 여기서 부터 각 단어 검색
for i in range(C):
    for k in range(Nlist[i]):
        for j in range(5):
            for p in range(5):
                ret = ''
                if Board[i][j][p] == Words[i][k][0]:
                    ret = recur(Board[i],(j,p),Words[i][k])
                
                if ret == 'YES':
                    break
            if ret == 'YES':
                break
        if ret == 'YES':
            print(Words[i][k],ret)
        else:
            print(Words[i][k],'NO')




