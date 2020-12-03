import sys
sys.setrecursionlimit(1000000)

def recur(mp,y,x,n):
    global cache
    
    if y >= n or x >= n:
        return 0
    if cache[y][x] == 0:
        return 0
    if cache[y][x] == 1:
        return 1
    if mp[y][x] == 0:
        return 1

    curr = mp[y][x]
    res = recur(mp,y+curr,x,n) or recur(mp,y,x+curr,n)
    if res:
        cache[y][x] = 1
    else:
        cache[y][x] = 0
    
    return res


C = int(sys.stdin.readline().strip())
for i in range(C):
    global cache
    cache = [[-1 for i in range(100)] for j in range(100)]
    n = int(sys.stdin.readline().strip())
    mp = [[] for i in range(n)]
    for j in range(n):
        mp[j] = list(map(int,sys.stdin.readline().strip().split()))
    result = recur(mp,0,0,n)
    if result == 0:
        print("NO")
    else:
        print("YES")