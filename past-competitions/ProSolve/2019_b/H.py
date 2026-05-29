T = int(input())

for _ in range(T):
    s = input()
    vis = set()
    for c in s:
        if c in vis:
            print(c); break
        vis.add(c)
    else:
        print("None")