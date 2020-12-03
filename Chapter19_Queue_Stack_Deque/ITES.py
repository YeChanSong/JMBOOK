
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
# 테스트 케이스의 수 입력

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