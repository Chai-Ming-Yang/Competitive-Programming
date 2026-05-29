import math
T = int(input())

special_points = {
    (1, 1): 4, 
    (1, 0): 3, 
    (0, 1): 3, 
    (2, 2): 4
}

for _ in range(T):
    a = input()
    dx = abs(ord(a[0]) - ord('A'))
    dy = abs(ord(a[1]) - ord('1'))

    if (dx, dy) in special_points:
        print(special_points[(dx,dy)]); continue

    moves = max(math.ceil(dx / 2.0),
                math.ceil(dy / 2.0),
                math.ceil((dx+dy) / 3.0))
    if (dx + dy) % 2 == 0:
        moves += 1

    print(moves)