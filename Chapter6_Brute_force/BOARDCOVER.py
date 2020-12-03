import sys
sys.setrecursionlimit(1000000)

def recur(coord,block=None):
    global H,W
    total = 0
    if block != None:
        for i in block:
            if i not in coord:
                return 0
            coord.remove(i)
    if len(coord) == 0:
        return 1    
    
    y,x = coord[0]
    total = recur(coord.copy(),[(y-1,x-1),(y-1,x),(y,x)]) + recur(coord.copy(),[(y-1,x-1),(y,x-1),(y,x)])\
        + recur(coord.copy(),[(y-1,x+1),(y-1,x),(y,x)]) + recur(coord.copy(),[(y-1,x+1),(y,x+1),(y,x)])\
        + recur(coord.copy(),[(y,x-1),(y+1,x-1),(y,x)]) + recur(coord.copy(),[(y+1,x),(y+1,x-1),(y,x)])\
        + recur(coord.copy(),[(y+1,x+1),(y,x+1),(y,x)]) + recur(coord.copy(),[(y+1,x+1),(y+1,x),(y,x)])\
        + recur(coord.copy(),[(y-1,x),(y,x-1),(y,x)]) + recur(coord.copy(),[(y,x+1),(y-1,x),(y,x)])\
        + recur(coord.copy(),[(y,x-1),(y+1,x),(y,x)]) + recur(coord.copy(),[(y+1,x),(y,x+1),(y,x)])
    
    return total
    
    

C = int(input())

for i in range(C):
    global H,W
    H,W = map(int,input().split())
    cntr = 0
    coord = []
    for j in range(H):
        init = input()
        for k in range(len(init)):
            if init[k] == '.':
                cntr += 1
                coord.append((j,k))
    
    if cntr %3 == 0:
        answer = recur(coord)
    else:
        answer = 0
    print(answer)