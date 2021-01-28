import sys, heapq
INF = float('inf')
def dijkstra(idx):
    global adj, pq, N, INF
    dist = [INF] * N
    dist[idx] = 1.0
    heapq.heappush(pq,(1.0,idx))
    while pq:
        cost, here = heapq.heappop(pq)
        if dist[here] < cost:
            continue
        for there, nextDist in adj[here]:
            nextDist *= cost
            if dist[there] > nextDist:
                dist[there] = nextDist
                heapq.heappush(pq,(nextDist,there))
    return dist
    
C = int(sys.stdin.readline().strip())
for k in range(C):
    N,M = map(int,sys.stdin.readline().strip().split())
    adj = list([] for i in range(N))
    pq = list()
    for i in range(M):
        s,d,n = sys.stdin.readline().strip().split()
        s,d = int(s), int(d)
        n = float(n)
        adj[s].append((d,n))
        adj[d].append((s,n))
    
    dist = dijkstra(0)
    print("%0.10f"%dist[N-1])