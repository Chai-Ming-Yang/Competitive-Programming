import heapq
n = int(input())
books = sorted([tuple(map(int, input().split())) for _ in range(n)])

time = res = 0
mn = []
for timeNeeded, due in books:

    while mn and -mn[0] > timeNeeded and (time + timeNeeded > due):
        time -= heapq.heappop(mn)
    if time + timeNeeded <= due:
        time += timeNeeded
        heapq.heappush(mn, -timeNeeded)
    res = max(res, len(mn))

print(res)