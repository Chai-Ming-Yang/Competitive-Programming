a = list(map(int, input().split()))

while a:
    for i in range(len(a) - 1):
        a[i] = a[i] - a[i+1]
        if a[i] < 0: a[i] = -a[i]
    a.pop()
    print(*a)