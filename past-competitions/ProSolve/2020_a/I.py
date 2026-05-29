from collections import defaultdict
N, K = map(int, input().split())

child = defaultdict(list)
for _ in range(N-1):
    u, v = map(int,input().split())
    child[u].append(v)

res = 0
path = []
def dfs(u):
    global res
    for node in path:
        if abs(u - node) <= K: res += 1
    path.append(u)
    for v in child[u]:
        dfs(v)
    path.pop()

dfs(1)
print(res)