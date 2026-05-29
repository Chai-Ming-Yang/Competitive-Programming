P = int(input())
points = []
for _ in range(P):
    points.append(tuple(map(int, input().split())))

N = 11
nearest = [ [[] for _ in range(N)] for _ in range(N) ]
for i in range(N):
    for j in range(N):
        dists = sorted( ((abs(i-x) + abs(j-y), c) for x, y, c in points),
                        key=lambda a: a[0] )

        pref = [0]
        for _, c in dists:
            pref.append(pref[-1] + (c==1))

        nearest[i][j] = pref

T = int(input())
for case in range(1, T+1):
    i, j, k = map(int, input().split())
    ones = nearest[i][j][k]
    print(f'Case #{case}: {1 if ones > k - ones else 2}')