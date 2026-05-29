from collections import deque
T = int(input())
for _ in range(T):
    N, k = map(int, input().split())
    a = [False] * N
    q = deque([])

    sprinklers = list(map(int, input().split()))
    for idx in sprinklers:
        a[idx-1] = True
        q.append(idx-1)
    t = 0
    while q:
        t += 1
        for _ in range(len(q)):
            u = q.popleft()
            if u-1 >=0 and not a[u-1]:
                q.append(u-1)
                a[u-1] = True
            if u+1 < N and not a[u+1]:
                q.append(u+1)
                a[u+1] = True
    print(t)