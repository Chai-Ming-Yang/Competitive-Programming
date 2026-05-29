from collections import defaultdict, deque
R, C = map(int, input().split())
g = [input() for _ in range(R)]

portal = defaultdict(list)
for r in range(R):
    for c in range(C):
        if g[r][c] == 'S': start = (r, c)
        elif g[r][c].islower(): portal[g[r][c]].append((r,c))

DIRS = [(0,1), (0,-1), (1,0), (-1,0)]

def bfs(sr, sc):
    q = deque([(sr, sc)])
    vis = [[False] * C for _ in range(R)]
    portal_used = set()

    def invalid(r,c):
        return (r<0 or r==R or c<0 or c==C or
                vis[r][c] or g[r][c] == '#')

    dist = 0
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            ch = g[r][c]
            if ch == 'E': return dist
            if ch.islower() and ch not in portal_used:
                for nr, nc in portal[ch]:
                    if invalid(nr,nc): 
                        continue
                    q.append((nr, nc))
                    vis[nr][nc] = True
                portal_used.add(ch)
            
            for dr, dc in DIRS:
                nr, nc = r+dr, c+dc
                if invalid(nr, nc): continue
                q.append((nr, nc))
                vis[nr][nc] = True

        dist += 1
    return -1

print(bfs(*start))