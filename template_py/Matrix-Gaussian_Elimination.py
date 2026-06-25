DIM = int(input())
G = [list(map(int, input().split())) for _ in range(DIM)]

# Forward Elimination
for PIV in range(DIM):
  parpiv = PIV
  for r in range(PIV+1, DIM):
    if abs(G[r][PIV]) > abs(G[parpiv][PIV]):
      parpiv = r
  G[PIV], G[parpiv] = G[parpiv], G[PIV]

  for r in range(PIV+1, DIM):
    factor = G[r][PIV] / G[PIV][PIV]
    for c in range(PIV, DIM+1):
      G[r][c] -= factor * G[PIV][c]

# Backward Propagation
res = [0] * DIM
for PIV in range(DIM-1, -1, -1):
  res[PIV] = G[PIV][DIM]
  for c in range(PIV+1, DIM):
    res[PIV] -= G[PIV][c] * res[c]
  res[PIV] /= G[PIV][PIV]
