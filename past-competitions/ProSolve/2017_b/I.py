T = input()
N = int(input())
sToR = {}
for _ in range(N):
    S, R = input().split()
    sToR[S] = R

res = []    
for c in T:
    if c in sToR:
        c = sToR[c]
    res.append(c)
print(''.join(res))