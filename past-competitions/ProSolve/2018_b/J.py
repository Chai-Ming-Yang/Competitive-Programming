from collections import defaultdict
n, k, d = map(int, input().split())

trees = [0] * (n+1)
count = defaultdict(int)
count[0] = n

for _ in range(d):
    a, b, h = map(int, input().split())
    for i in range(a, b+1):
        count[trees[i]] -= 1
        if not count[trees[i]]: del count[trees[i]]

        trees[i] = (trees[i] + h) % k

        count[trees[i]] += 1
    print(len(count))