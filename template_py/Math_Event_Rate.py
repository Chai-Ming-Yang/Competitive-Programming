import math
LCM = math.lcm(x, y)
x_tick = LCM // x
y_tick = LCM // y

num_evt = lambda t: t//x_tick + t//y_tick + t//LCM

cycle_len = num_evt(LCM)

t = 0
cycle = []
while len(cycle) < cycle_len:
    t += 1
    if t % LCM == 0:
        cycle.append('both')
    elif t % tick_x == 0:
        cycle.append('x')
    elif t % tick_y == 0:
        cycle.append('y')
ans = cycle[(k-1) % cycle_len]
