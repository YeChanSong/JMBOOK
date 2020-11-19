import sys
sys.setrecursionlimit(10000000)

def recur(N,li,start,end):
    global cache
    if start != end:
        m = (start + end)//2
        return max(recur(N,li,m+1,end), recur(N,li,start,m))
    cnt = 0
    for i in range(start,N-1):
        cnt +=1
        
        if cache[i+1] != None and li[i] < li[i+1]:
            tmp = cache[i+1] + cnt
            
            cache[start] = tmp
            return tmp
        if li[i] >= li[i+1]:
            cache[start] = cnt
            return cnt
    cache[start] = cnt+1
    return cnt+1

C = int(sys.stdin.readline().strip())
for i in range(C):
    N = int(sys.stdin.readline().strip())
    li = list(map(int,sys.stdin.readline().strip().split()))
    cache = [None for i in range(N)]
    ans = recur(N,li,0,N-1)
    print(ans)