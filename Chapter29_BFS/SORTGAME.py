import sys
from collections import deque

def precalc(n):
    global toSort
    srtd = tuple(i for i in range(n))
    q = deque()
    q.append(srtd)
    toSort.setdefault(srtd,0)
    while len(q) != 0:
        here = q.popleft()
        cost = toSort[here]
        here = list(here)
        for i in range(n):
            for j in range(i+2,n+1):
                tmp = here[i:j]
                tmp.reverse()
                for k in range(j-i):
                    here[i+k] = tmp[k]
                if toSort.get(tuple(here)) == None:
                    toSort.setdefault(tuple(here),cost+1)
                    q.append(tuple(here))
                tmp = here[i:j]
                tmp.reverse()
                for k in range(j-i):
                    here[i+k] = tmp[k]
    
def solve(perm):
    global toSort
    n = len(perm)
    fixed = list(0 for i in range(n))
    for i in range(n):
        smaller = 0
        for j in range(n):
            if perm[j] < perm[i]:
                smaller+=1
        fixed[i] = smaller
    return toSort[tuple(fixed)]

C = int(sys.stdin.readline().strip())
for i in range(C):
    N = int(sys.stdin.readline().strip())
    init = list(sys.stdin.readline().strip().split())
    toSort = dict()
    precalc(N)
    ans = solve(init)
    print(ans)