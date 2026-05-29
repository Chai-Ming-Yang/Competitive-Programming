T = int(input())
res = []
for _ in range(T):
    a = input().split()
    for i in range(len(a)):
        s = a[i]
        if a[0].isalpha():
            a[i] = s[0].upper() + s[1:]
    res.append(' '.join(a))

for ans in res:
    print(ans)