import sys, heapq
INF = 1e100
def total():
    global trgt, station,V
    ans = 0
    li = dijkstra(V)
    for i in trgt:
        ans += li[i-1]
    return ans

def dijkstra(src):
    global adj,V
    pq = list()
    dist = list(INF for i in range(V+1))
    dist[src] = 0
    heapq.heappush(pq,(0,src))

    while pq:
        cost, here = heapq.heappop(pq)
        
        if dist[here] < cost:
            continue
        
        for there, nextDist in adj[here]:
            nextDist += cost
            
            if nextDist < dist[there]:
                dist[there] = nextDist
                heapq.heappush(pq,(nextDist,there))
    return dist

C = int(sys.stdin.readline().strip())
for i in range(C):
    V,E,n,m = map(int,sys.stdin.readline().strip().split())
    adj = list([] for i in range(E))
    for j in range(E):
        s,d,t = map(int,sys.stdin.readline().strip().split())
        adj[s-1].append((d-1,t))
        adj[d-1].append((s-1,t))
    trgt = list(map(int,sys.stdin.readline().strip().split()))
    station = list(map(int,sys.stdin.readline().strip().split()))
    for i in station:
        adj[V].append((i-1,0))
    '''
    처음에는 모든 화재장소에서 다익스트라를 통해 가장 가까운 소방서를 찾는 방식으로 진행. -> 시간초과
    그래프에 모든 소방서와 연결된 정점을 추가해서 한번의 다익스트라로 모든 화재장소와
    연결된 최단 경로를 구할 수 있었다.
    
    항상 시간초과가 발생하는 문제에 대해서는 그래프를 변형할 여지가 있는지 확인하자.
    ''' 
    ans = total()
    print(ans)