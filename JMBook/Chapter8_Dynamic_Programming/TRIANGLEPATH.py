import sys
sys.setrecursionlimit(1000000)

def recur(n,line,y,x):
    global cache
    if y == n:
        return 0
    
    if cache[y][x] != -1:
        return cache[y][x]
    
    rtn = line[y][x] + max(recur(n,line,y+1,x),recur(n,line,y+1,x+1))
    cache[y][x] = rtn
    return rtn



C = int(sys.stdin.readline().strip())
for i in range(C):
    n = int(sys.stdin.readline().strip())
    line = []
    for j in range(n):
        tmp = list(map(int,sys.stdin.readline().strip().split()))
        line.append(tmp)
    cache =[[-1 for j in range(i)] for i in range(1,n+1)]
    print(recur(n,line,0,0))