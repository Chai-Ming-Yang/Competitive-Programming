n = int(input())
k = int(input())
CHAR = [chr(i + ord('0')) for i in range(k)]

if n==1: print('\"' + ''.join(CHAR) + '\"'); exit()

adj = {}
def build(s):
    global n
    if len(s) == n-1:
        adj[s] = CHAR[:]
        return
    for c in CHAR:
        build(s+c)
build('')


import sys
sys.setrecursionlimit(10**7)
path = []
def dfs(u):
    while adj[u]:
        v = adj[u].pop()
        dfs(u[1:] + v)
        path.append(v)
dfs('0'*(n-1))
path.reverse()

print('\"' + '0'*(n-1)+''.join(path) + '\"')