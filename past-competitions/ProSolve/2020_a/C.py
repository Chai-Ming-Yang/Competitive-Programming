import heapq
T = int(input())
o = ord('a') - 1

res = []
mn = [0] * 3
for _ in range(T):
    N = int(input())
    for _ in range(N):
        s = input().lower()
        total = 0
        for c in s:
            total += (ord(c) - o)
        if mn[0] < total:
            heapq.heappush(mn, total)
            heapq.heappop(mn)
    res.append(str(sum(mn)))

print('\n'.join(res))