from collections import defaultdict

N = int(input())    # num nodes
H = int(input())    # src
P = int(input())
adj = defaultdict(list)

for _ in range(P):
    s, d, c = map(int, input().split())
    adj[s].append((d, c))
    adj[d].append((s, c))

res = float('inf')
vis = set()

def dfs(u, cost):
    global res, H
    if len(vis) == N and u == H:
        res = min(res, cost)
        return
    if u in vis: return 
    vis.add(u)
    for v, w in adj[u]:
        if cost + w > res: continue
        dfs(v, cost + w)
    vis.remove(u)


dfs(H, 0)
print(res)