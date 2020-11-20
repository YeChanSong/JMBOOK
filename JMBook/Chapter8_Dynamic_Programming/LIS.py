import sys
sys.setrecursionlimit(10000000)

def recur(N,li,start):
    global cache
    '''
    캐시에는 수열 오른쪽으로 자신보다 큰 원소의 갯수 +1를 담는다
    자신보다 큰 원소의 수는 곧 순증가를 판단하기 위한 기준이다.
    +1은 자신을 순증가 수열에 추가했을 때를 나타낸다.
    따라서, 순증가 수열의 최대 길이를 캐시에 저장하게 된다
    '''
    if start < 0:
        return 0
    mxche = 0
    '''
    수열의 오른쪽 끝부터 왼쪽 끝으로 진행
    각 원소에서는 수열의 오른쪽으로 진행하면서 자신보다 큰 원소를 만날 경우
    해당 원소의 캐시값을 mxche에 저장한다. 이러한 방식으로
    원소는 자신보다 큰 원소의 캐시값중 가장 큰 값 +1을 자신의 캐시에 저장한다.
    '''
    for i in range(start+1,N):
        if li[i] > li[start]:
            if cache[i] > mxche:
                mxche = cache[i]
            else:
                continue
        else:
            continue
    cache[start] = mxche+1
    recur(N,li,start-1) 
    

C = int(sys.stdin.readline().strip())
for i in range(C):
    N = int(sys.stdin.readline().strip())
    li = list(map(int,sys.stdin.readline().strip().split()))
    cache = [None for i in range(N)]
    recur(N,li,N-1)
    ans = max(cache)
    print(ans)