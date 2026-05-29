import math
n = int(input())
x, y, r = map(int, input().split())

for _ in range(n):
    i, j = map(int, input().split())
    if math.sqrt((x-i)**2 - (y-j)**2) < r:
        print("ALERT")
        break