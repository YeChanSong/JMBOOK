
from collections import deque

def signalGen():
    t2mp = 1983
    while 1:
        tmp = t2mp%10000 +1
        result = tmp
        yield result
        t2mp = (t2mp * 214013 + 2531011) % 2**32
        
# 제너레이터로 신호생성

C = int(input())
# 테스트 케이스의 수 입력C = int(input())
# 테스트 케이스의 수 입력

for i in range(C):

    K, N = map(int,input().split())
    tmp = []
    t2mp = 1983
    for j in range(1,N+1):
        tmp.append(t2mp%10000 +1)
        t2mp = (t2mp * 214013 + 2531011) % 2**32
        #print(t2mp)
        # t2mp에 신호 기록 생성해서 저장
        
        # tmp에 입력 신호 생성해서 저장
    #print(tmp)
    # 여기까지 입력 신호 생성
    cnt = 0
    # 부분 수열의 합이 K값과 일치할 경우 cnt 증가
    
    for k in range(1,N+1):
        subtotal = 0
        idx = 0
        for a in range(k):
            subtotal += tmp[a]
            idx = a
        # 최초 k 크기 만큼의 부분 합
        for a in range(len(tmp)):
            if subtotal == K:
                cnt += 1
            idx += 1
            if idx == len(tmp):
                break
            subtotal -= tmp[a]
            subtotal += tmp[idx]
    print(cnt)

for i in range(C):

    K, N = map(int,input().split())
    
    cnt =0
    subtotal = 0
    queue = deque()
    # 부분 수열의 합이 K값과 일치할 경우 cnt 증가
    signal = signalGen()
    for i in range(N):
        sig = next(signal)
        subtotal += sig
        queue.append(sig)
        
        while subtotal > K:
            subtotal -= queue.popleft()
            
        if subtotal == K:
            cnt += 1
    print(cnt)