import sys
sys.setrecursionlimit(100000)

def recur(boardnum,recurnum,letters):
    '''
    boardnum: 게임판 번호, 
    recurnum: 단어에서 찾아야 할 나머지 글자 수,
    letters: 찾아야 할 글자들
    '''
    
    
    
    
    
    


C = int(input())
# 테스트 케이스의 수
GameBoard = list()
# BOGGLE 게임 판
N = list()
# 각 케이스 별 찾을 글자 수 N
Words = list()
# 단어와 YES, NO를 묶을 dict를 저장할 Words 리스트
count = list()
# 단어의 수 저장할 리스트

for i in range(C):
    # 테스트 케이스 입력 처리
    tmpBoard = list()
    for j in range(5):
        # 각 테스트 케이스 별 게임판 처리
        tmpBoard.append(input())
    GameBoard.append(tmpBoard)
    # 단어의 수 cnt에 입력
    cnt = int(input())
    count.append(cnt)
    tmpWords = dict()
    for k in range(cnt):
        # 단어 입력 처리
        tmpWords[input()] = 'NO'
    Words.append(tmpWords)

for i in range(C):
    # 각 테스트 케이스 처리
    for j in range(count[i]):
        # 단어 수 만큼 반복하며 만들 수 있는지 여부 확인
        recur(i,len(Words[i][j]),Words[i][j])