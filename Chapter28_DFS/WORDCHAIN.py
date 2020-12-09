import sys
sys.setrecursionlimit(1000000)

def dfsAll():
    global adj, visited
    
    for i in range(len(adj)):
        if visited[i] == True:
            continue
        dfs(i)

def dfs(pos):
    global adj, answer, visited, words
    visited[pos] = True
    for i in range(len(adj[pos])):
        if adj[pos][i] == True and visited[i] == False:
            dfs(i)
    answer.append(words[pos])
    
def graphBuilder():
    global words, adj
    for i in range(len(words)):
        for j in range(len(words)):
            if j == i:
                continue
            if words[i][-1] == words[j][0]:
                adj[i][j] = True

C = int(sys.stdin.readline().strip())
for i in range(C):
    N = int(sys.stdin.readline().strip())
    words = []
    for j in range(N):
        words.append(sys.stdin.readline().strip())
    adj = [[False for i in range(N)] for j in range(N)]
    answer = []
    visited = [False for i in range(N)]
    graphBuilder()
    dfsAll()
    flag = True
    '''
    for j in range(len(answer)-1):
        if answer[j][0] != answer[j+1][-1]:
            answer = 'IMPOSSIBLE'
            flag = False
            break
    if flag == True:
        answer = ' '.join(reversed(answer))
    print(answer)
    '''
    answer = list(reversed(answer))
    for k in range(len(answer)-1):
        if answer[k][-1] != answer[k+1][0]:
            answer = 'IMPOSSIBLE'
            flag = False
            break
    if flag == True:
        answer = ' '.join(answer)
    print(answer)