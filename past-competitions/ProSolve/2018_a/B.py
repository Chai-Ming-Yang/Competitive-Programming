import math
n, x, y = map(int, input().split())
LCM = math.lcm(x, y)
x, y = LCM//x, LCM//y

cycle_len = x + y - 1
cycle = []
t = 1
while len(cycle) < cycle_len:
    if t % x == 0 and t % y == 0:
        cycle.append("Both")
    elif t % x == 0:
        cycle.append("Jason")
    elif t % y == 0:
        cycle.append("Jimmy")
    t += 1

res = []
for i in range(n):
    tree = int(input())
    res.append(cycle[(tree - 1) % cycle_len])
for ans in res:
    print(ans)

# import math
# n, x, y = map(int, input().split())

# lcm = math.lcm(x, y)    # in unit time

# jx = lcm // x   # in unit chop
# jy = lcm // y

# cycle_len = (lcm//jx) + (lcm//jy) - 1

# cycle = []
# t = 1
# while len(cycle) < cycle_len:
#     if t % jx == 0 or t % jy == 0:
#         cycle.append("Both")
#     elif t % jx == 0:
#         cycle.append("Jason")
#     elif t % jy == 0:
#         cycle.append("Jimmy")
#     t += 1

# for _ in range(n):
#     h = int(input())
#     print(cycle[(h-1) % cycle_len])