n = int(input())

a = list(map(int, input().split()))
pre = a[:]
for i in range(1, n):
    pre[i] += pre[i-1]
    
res = 0
for i in range(n):
    if pre[i] == (pre[-1] // 2):
        res += 1
print(res)
