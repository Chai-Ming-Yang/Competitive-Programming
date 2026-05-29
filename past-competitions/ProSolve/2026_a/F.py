class RollbackDSU:
    def __init__(self, n):
        self.par = list(range(n))
        self.sz = [1] * n
        self.hist = []
        self.comp = n
    def find(self, a):
        while a != self.par[a]:
            a = self.par[a]
        return a
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:  return False
        if self.sz[a] < self.sz[b]:
            a, b = b, a
        self.hist.append((b, self.par[b], a, self.sz[a]))
        self.par[b] = a
        self.sz[a] += self.sz[b]
        self.comp -= 1
        return True
    def snapshot(self):
        return len(self.hist)
    def rollback(self, snap):
        while len(self.hist) > snap:
            b, pb, a, sa = self.hist.pop()
            self.par[b] = pb
            self.sz[a] = sa
            self.comp += 1

n, q = map(int, input().split())
ops = []
for _ in range(q):
    s = input().split()
    if s[0] == '?':
        ops.append(('?',))
    else:
        t, u, v = s
        u = int(u) -1
        v = int(v) -1
        if u > v:
            u, v = v, u
        ops.append((t, u, v))

seg = [[] for _ in range(4*q)]
def add(node, nl, nr, l, r, edge):
    if r <= nl or nr <= l: return
    if l <= nl and nr <= r:
        seg[node].append(edge)
        return
    mid = (nl + nr) // 2
    add(node*2, nl, mid, l, r, edge)
    add(node*2 + 1, mid, nr, l, r, edge)

def dfs(node, nl, nr):
    snap = dsu.snapshot()
    for u, v in seg[node]:
        dsu.union(u, v)
    if nl + 1 == nr:
        if ops[nl][0] == '?':
            ans.append(dsu.comp)
    else:
        mid = (nl + nr) // 2
        dfs(node*2, nl, mid)
        dfs(node*2 + 1, mid, nr)
    dsu.rollback(snap)

start = {}

for t, op in enumerate(ops):
    if op[0] == '+':
        _, u, v = op
        start[(u,v)] = t
    elif op[0] == '-':
        _, u, v = op
        l = start.pop((u, v))
        add(1, 0, q, l, t, (u, v))

for edge, l in start.items():
    add(1, 0, q, l, q, edge)

dsu = RollbackDSU(n)
ans = []

dfs(1, 0, q)
print(*ans, sep='\n')
