par = list(range(n))
sz= [1] * n
def find(a):
  while a != par[a]:
    par[a] = par[par[a]]
    a = par[a]
  return a

def union(a, b):
  a, b = find(a), find(b)
  if a == b: return False
  if sz[a] < sz[b]:
    a, b = b, a
  par[b] = a
  sz[a] += sz[b]
  return True
