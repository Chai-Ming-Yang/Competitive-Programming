from collections import deque

MOD = 10**9 + 7
NINF = -10**18
n, m = map(int, input().split())

adj = [[] for _ in range(n+1)]
indeg = [0] * (n+1)
for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    indeg[v] += 1

topo = []
q = deque([i for i in range(1, n+1) if indeg[i] == 0])
while q:
    u = q.popleft()
    topo.append(u)
    for v, _ in adj[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)

dist = [NINF] * (n+1)
ways = [0] * (n+1)
dist[1] = 0
ways[1] = 1

for u in topo:
    if dist[u] == NINF: continue
    for v, w in adj[u]:
        nd = dist[u] + w
        if nd > dist[v]:
            dist[v] = nd
            ways[v] = ways[u]
        elif nd == dist[v]:
            ways[v] = (ways[v] + ways[u]) % MOD

if ways[n] == 0:
    print(-1)
else:
    print(dist[n], ways[n])