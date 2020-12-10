import sys
sys.setrecursionlimit(1000000)

def getEulerTrailOrCircuit():
    global adj, indegree, outdegree
    for i in range(26):
        if outdegree[i] == indegree[i]+1:
            getEulerCircuit(i)
            return
        
    for i in range(26):
        if outdegree[i] != 0:
            getEulerCircuit(i)
            return
    
def getEulerCircuit(pos):
    global adj, answer
    for i in range(len(adj)):
        while adj[pos][i]>0:
            adj[pos][i] -=1
            getEulerCircuit(i)
    answer.append(pos)
    
def makeGraph():
    global words, adj, graph, indegree, outdegree
    for i in range(len(words)):
        a = ord(words[i][0]) - ord('a')
        b = ord(words[i][-1]) - ord('a')
        graph[a][b].append(words[i])
        adj[a][b]+=1
        outdegree[a]+=1
        indegree[b]+=1
        
def checkEuler():
    global answer
    plus1 = 0
    minus1 = 0
    for i in range(26):
        delta = outdegree[i] - indegree[i]
        if delta < -1 or delta > 1:
            return False

        if delta == 1:
            plus1+=1
        if delta == -1:
            minus1+=1
        
    return (plus1 == 1 and minus1 == 1) or (plus1 == 0 and minus1 == 0)

C = int(sys.stdin.readline().strip())
for i in range(C):
    N = int(sys.stdin.readline().strip())
    words = []
    for j in range(N):
        words.append(sys.stdin.readline().strip())
    
    indegree, outdegree = [0 for i in range(26)], [0 for i in range(26)]
    graph = [[[] for i in range(26)] for j in range(26)]
    adj = [[0 for i in range(26)] for i in range(26)]
    answer = []
    
    makeGraph()
    if checkEuler() == False:
        print("IMPOSSIBLE")
    else:
        getEulerTrailOrCircuit()
        if len(answer) != len(words)+1:
            print("IMPOSSIBLE")
        else:
            answer = list(reversed(answer))
            ret = ''
            for i in range(1,len(answer)):
                a = answer[i-1]
                b = answer[i]
                if len(ret) != 0:
                    ret += ' '
                ret += graph[a][b].pop()
            print(ret)