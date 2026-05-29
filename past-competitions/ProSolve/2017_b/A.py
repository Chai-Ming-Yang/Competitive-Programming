T = int(input())
res = []
for _ in range(T):
    A, B, S = map(int, input().split())
    res.append(' '.join([str(i) for i in range(A, B+1, S)]))

for ans in res:
    print(ans)