T = int(input())

for _ in range(T):
    n = int(input())
    i = 1
    while n != 6174:
        m = ''.join(sorted(str(n)))
        n = int(m[::-1]) - int(m)
        i += 1
    print(i)