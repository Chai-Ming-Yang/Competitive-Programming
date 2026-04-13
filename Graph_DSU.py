par = list(range(n))
sz= [1] * n
def find(a):
  while a != par[x]:
    par[a] = par[par[x]]
    x = par[x]
  return x

def union(a, b):
  a, b = find(a), find(b)
  if a == b: return False
  if sz[a] < sz[b]:
    a, b = b, a
  par[b] = a
  sz[a] += sz[b]
  return True
