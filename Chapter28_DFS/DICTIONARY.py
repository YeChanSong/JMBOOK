import sys,re
sys.setrecursionlimit(1000000)

def dfsall():
    global adj,visited,tpsort
    
    for k in adj.keys():
        if visited[k] == True:
            continue
        dfs(k)
        

def dfs(ch):
    global adj,visited,tpsort
    '''
    ch: dfs를 시작할 정점의 글자
    '''
    visited[ch] = True
    
    for i in adj[ch]:
        if visited[i] == True:
            continue
        dfs(i)
    tpsort.append(ch)

def cmpr():
    global adj,dic,tpsort
    '''
    사전의 글 순서를 비교하고 인접 리스트 작성
    '''
    for i in range(len(dic)-1):
        l = len(dic[i]) < len(dic[i+1]) and len(dic[i]) or len(dic[i+1])
        
        for j in range(l):
            if dic[i][j] != dic[i+1][j]:
                #adj.setdefault(dic[i][j],set())
                #adj.setdefault(dic[i+1][j],set())
                adj[dic[i][j]].add(dic[i+1][j])
                
                break


C = int(sys.stdin.readline().strip())
for i in range(C):
    N = int(sys.stdin.readline().strip())
    dic = []
    for j in range(N):
        dic.append(sys.stdin.readline().strip())
    
    adj = {k: set() for k in 'abcdefghijklmnopqrstuvwxyz'}
    visited = {k: False for k in 'abcdefghijklmnopqrstuvwxyz'}
    tpsort = []
    cmpr()
    dfsall()
    srtd = reversed(tpsort)
    srtd = ''.join(srtd)
    flag = True
    for i in range(len(srtd)):
        for j in adj[srtd[i]]:
            if i > srtd.index(j):
                print("INVALID HYPOTHESIS")
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(srtd)
