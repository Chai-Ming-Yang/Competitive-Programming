N = int(input())
A = list(map(int, input().split()))
M = int(input())
P = list(map(int, input().split()))

A.sort(reverse=True)
total = sum(A)
for p in P:
    print(total - A[p-1])