import sys
sys.setrecursionlimit(10000000)

def recur(idx):
    global cache, pi
    if idx >= len(pi):
        return 123456789
    
    if cache[idx] != None:
        return cache[idx]
    
    
    diff = [123456789 for i in range(3)]
    end = len(pi) - idx
    if end > 2:
        if pi[idx+0] == pi[idx+1] == pi[idx+2]:
            diff[0] = 1
        elif pi[idx+0] == pi[idx+2] != pi[idx+1]:
            diff[0] = 4
        elif abs(int(pi[idx+0]) - int(pi[idx+1])) == abs(int(pi[idx+1]) - int(pi[idx+2])) == 1:
            diff[0] = 2
        elif int(pi[idx+0]) - int(pi[idx+1]) == int(pi[idx+1]) - int(pi[idx+2]):
            diff[0] = 5
        else:
            diff[0] = 10
    if end > 3:
        if pi[idx+0] == pi[idx+1] == pi[idx+2] == pi[idx+3]:
            diff[1] = 1
        elif pi[idx+0] == pi[idx+2] and pi[idx+1] == pi[idx+3]:
            diff[1] = 4
        elif abs(int(pi[idx+0]) - int(pi[idx+1])) == abs(int(pi[idx+1]) - int(pi[idx+2])) == \
            abs(int(pi[idx+2]) - int(pi[idx+3])) == 1:
            diff[1] = 2
        elif int(pi[idx+0]) - int(pi[idx+1]) == int(pi[idx+1]) - int(pi[idx+2]) == int(pi[idx+2]) - int(pi[idx+3]):
            diff[1] = 5
        else:
            diff[1] = 10
    if end > 4:
        if pi[idx+0] == pi[idx+1] == pi[idx+2] == pi[idx+3] == pi[idx+4]:
            diff[2] = 1
        elif pi[idx+0] == pi[idx+2] == pi[idx+4] and pi[idx+1] == pi[idx+3]:
            diff[2] = 4    
        elif abs(int(pi[idx+0]) - int(pi[idx+1])) == abs(int(pi[idx+1]) - int(pi[idx+2])) == \
            abs(int(pi[idx+2]) - int(pi[idx+3])) == abs(int(pi[idx+3]) - int(pi[idx+4])) == 1:
            diff[2] = 2
        elif int(pi[idx+0]) - int(pi[idx+1]) == int(pi[idx+1]) - int(pi[idx+2]) ==\
            int(pi[idx+2]) - int(pi[idx+3]) == int(pi[idx+3]) - int(pi[idx+4]):
            diff[2] = 5
        else:
            diff[2] = 10
    
    mdiff = min(diff)
    
    a = min(recur(idx+3),recur(idx+4),recur(idx+5))
    if a == 123456789:
        a = 0
    
    stp = mdiff + a
    cache[idx] = stp
    return stp
    

C = int(sys.stdin.readline().strip())
for i in range(C):
    pi = sys.stdin.readline().strip()
    cache = [None for i in range(len(pi))]
    ans = recur(0)
    print(ans)