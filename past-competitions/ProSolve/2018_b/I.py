T = int(input())
a = [int(input()) for _ in range(T)]

MAX_A = max(a)
isP = [True] * (MAX_A + 1)
isP[0] = isP[1] = False
factor = list(range(MAX_A + 1))

for i in range(2, MAX_A+1):
    if not isP[i]: continue
    for j in range(2*i, MAX_A+1, i):
        if isP[j]:
            isP[j] = False
            factor[j] = i

for n in a:
    if isP[n]: print('Prime')
    else: print(factor[n])