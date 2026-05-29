N = int(input())
auth = {}
for _ in range(N):
    usr, pas = input().split()
    auth[usr] = pas

T = int(input())
res = []
for _ in range(T):
    usr, pas = input().split()
    if auth.get(usr) == pas:
        res.append("YES")
    else:
        res.append("NO")
for ans in res:
    print(ans)