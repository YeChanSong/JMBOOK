import sys, heapq, math
INF = 1e200
def dijkstra(idx):
    global adj, pq, N, INF

    dist = list(INF for i in range(N))
    heapq.heappush(pq,(0,idx))
    while len(pq):
        cost, here = heapq.heappop(pq)
        if dist[here] < cost:
            continue
        for i in range(len(adj[here])):
            there, nextDist = adj[here][i]
            nextDist += cost
            if dist[there] > nextDist:
                dist[there] = nextDist
                heapq.heappush(pq,(nextDist,there))
    return dist
    
C = int(sys.stdin.readline().strip())
N,M = map(int,sys.stdin.readline().strip().split())
adj = list([] for i in range(N))
pq = list()
for i in range(M):
    s,d,n = sys.stdin.readline().strip().split()
    adj[int(s)].append((int(d),math.log10(float(n))))
    adj[int(d)].append((int(s),math.log10(float(n))))
    
dist = dijkstra(0)
print("%0.10f"%10**dist[N-1])