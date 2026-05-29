n = int(input())
a = list(map(int, input().split()))

if sum(a) < 0:
    print(-1); exit()

start = 0
found = False
while start < n and not found:
    cur = 0
    for i in range(n):
        cur += a[(start+i) % n]
        if cur < 0:
            start += i + 1
            break
    else:
        found = True

if found:   print(start+1)
else:   print(-1)