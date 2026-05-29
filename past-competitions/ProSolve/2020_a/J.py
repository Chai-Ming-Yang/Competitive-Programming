N = int(input())
a = list(map(int, input().split()))
if max(a) == N:
    print("Impossible"); exit()

b = [0] * N
freq = {}   # hat , num
hat = 1

for i in range(N):
    if a[i] not in freq:
        freq[a[i]] = [hat, N - a[i] - 1]
        hat += 1
    else:
        freq[a[i]][1] -= 1

    b[i] = freq[a[i]][0]
    if freq[a[i]][1] == 0:
        del freq[a[i]]

if freq:
    print("Impossible")
    exit()
print('Possible')
print(*b)