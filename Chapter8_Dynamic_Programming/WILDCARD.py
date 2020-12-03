import sys
sys.setrecursionlimit(1000000)

def recur(fname,idx):
    pass

C = int(sys.stdin.readline().strip())

for i in range(C):
    wcrd = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    fname = []
    for j in range(n):
        fname.append(sys.stdin.readline().strip())
    
    res = recur(fname,0)
    res = sorted(res)
    for j in res:
        print(j)