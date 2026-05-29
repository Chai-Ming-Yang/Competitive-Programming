""" higher h
    lower w
    longer d """
T = int(input())
participants = []
for id in range(1, T+1):
    pax = (id, *map(float, input().split()))
    participants.append(pax)

participants.sort(key=lambda a: (-a[1], a[2], -a[3]))
for i, h, w, l in participants:
    print(f'ID:{i} H:{h:.2f} W:{w:.2f} L:{l:.2f}')