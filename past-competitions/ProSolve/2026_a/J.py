""" Fenwick-Tree """


from bisect import bisect_left, bisect_right
from collections import defaultdict

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, v):
        while i <= self.n:
            self.bit[i] += v
            i += i & -i

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l-1)

n, q = map(int, input().split())
a = [0] + list(map(int, input().split()))

pos = defaultdict(list)
for i in range(1, n+1): pos[a[i]].append(i)
for k in pos: pos[k].sort()

bit = BIT(n)
last = [0] * (n+1)

def set_last(v):
    if not pos[v]: return
    i = pos[v][-1]
    if not last[i]:
        last[i] = 1
        bit.add(i, 1)

def unset_last(v):
    if not pos[v]: return
    i = pos[v][-1]
    if last[i]:
        last[i] = 0
        bit.add(i, -1)

for v in pos: set_last(v)

out = []

for _ in range(q):
    tmp = list(map(int, input().split()))

    if tmp[0] == 1:
        i, x = tmp[1], tmp[2]

        if a[i] == x: continue

        old = a[i]

        unset_last(old)

        idx = bisect_left(pos[old], i)
        pos[old].pop(idx)

        set_last(old)

        unset_last(x)

        arr = pos[x]
        j = bisect_left(arr, i)
        arr.insert(j, i)

        set_last(x)

        a[i] = x

    elif tmp[0] == 2:
        l, r = tmp[1], tmp[2]
        out.append(str(bit.range_sum(l, r)))

    else:
        l, r, f = tmp[1], tmp[2], tmp[3]

        arr = pos.get(f, [])

        L = bisect_left(arr, l)
        R = bisect_right(arr, r)

        out.append(str(R - L))

print("\n".join(out))