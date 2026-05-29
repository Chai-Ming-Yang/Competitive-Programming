import heapq
R, C = map(int, input().split())
g = [input() for _ in range(R)]

def findSrc():
    for r in range(R): 
        for c in range(C):
            if g[r][c] == 'D': return (r, c)

src = findSrc()
DIRS = {'D':(1, 0), 'U':(-1, 0), 
        'R':(0, 1), 'L':(0, -1)}
par = {}

def invalidNode(r, c):
    return (r<0 or r==R or c<0 or c==C or
            (r,c) in par or g[r][c] == '#')

pq = [(0, *src)]

while pq:
    dist, r, c = heapq.heappop(pq)

    for d, (dr, dc) in DIRS.items():
        nr, nc = r+dr, c+dc
        if invalidNode(nr, nc): continue
        
        par[(nr,nc)] = d
        if g[nr][nc] == 'C': 
            dst = [nr, nc]; pq = []; break

        if g[nr][nc] == 'S':
            heapq.heappush(pq, (dist + 5, nr, nc))
        else:
            heapq.heappush(pq, (dist + 1, nr, nc))

r, c = dst
path = []
while g[r][c] != 'D':
    path.append(par[(r, c)])
    dr, dc = DIRS[par[(r,c)]]
    r, c = r-dr, c-dc

print(''.join(reversed(path)))