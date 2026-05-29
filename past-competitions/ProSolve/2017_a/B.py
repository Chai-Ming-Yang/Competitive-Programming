T = int(input())
res = []

for _ in range(T):
    HH, MM = map(int, input().split(':'))
    """
    HH = -HH % 12
    MM = -MM % 60
    if MM:
        HH = (HH-1) % 12
    """
    total = HH * 60 + MM
    flipped = -total % (12 * 60)
    HH = flipped // 60
    MM = flipped % 60
    
    if HH == 0:
        HH = 12

    res.append(f'{HH:02d}:{MM:02d}')

for ans in res:
    print(ans)