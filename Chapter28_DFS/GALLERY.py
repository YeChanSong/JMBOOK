import sys
sys.setrecursionlimit(100000)

def graphBuilder():
    global li, adj
    
    for i in li:
        adj[i[0]].append(i[1])
        adj[i[1]].append(i[0])

def dfsAll():
    global adj, cams, G, visited
    
    for i in range(G):
        if visited[i] == False:
            if dfs(i) == 0:
                cams+=1

def dfs(idx):
    global adj, cams, visited
    # 결과로 반환되는 경우를 2가지로 나눌 수 없음.
    visited[idx] = True
    children = [0,0,0]
    for i in adj[idx]:
        if visited[i] == False:
            children[dfs(i)] +=1
    
    if children[0] != 0:
        cams+=1
        return 2
    if children[2] != 0:
        return 1
    return 0

C = int(sys.stdin.readline().strip())
for i in range(C):
    li = list()
    G,H = map(int,sys.stdin.readline().strip().split())
    for j in range(H):
        u,v = map(int,sys.stdin.readline().strip().split())
        li.append((u,v))
    visited = list(False for i in range(G))
    cams = 0
    adj = list([] for i in range(G))
    graphBuilder()
    dfsAll()
    #print(adj)
    #print(visited)
    print(cams)