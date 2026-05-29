T = int(input())

for _ in range(T):
    n = int(input())
    cur = 1
    for i in range(1, n+1):
        print(*list(range(cur, cur + i)))
        cur += i
    cur -= 1
    for i in range(n, 0, -1):
        print(*list(range(cur, cur - i, -1)))
        cur -= i
