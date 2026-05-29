import math
def dist(p1, p2):
    return math.sqrt( (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 )

def bruteforce(points):
    mn = float('inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            mn = min(mn, dist(points[i], points[j]))
    return mn

def closestPair(points):
    n = len(points)
    if n <= 3: return bruteforce(points)

    mid = n // 2
    mid_p = points[mid]
    lef, rig = points[:mid], points[mid:]

    d = min( closestPair(lef), closestPair(rig) )
    
    # filter x
    strip = [ p for p in points if abs(p[0] - mid_p[0]) < d ]
    # sort y
    strip.sort(key=lambda p: p[1])

    # check 7 points
    strip_len = len(strip)
    for i in range(strip_len):
        for j in range(i + 1 , min(i + 8, strip_len)):
            if strip[j][1] - strip[i][1] >= d:
                break
            d = min(d, dist(strip[i], strip[j]))
    return d

N = int(input())
points = [list(map(float, input().split())) for _ in range(N)]
points.sort()

print(f'{closestPair(points):.4f}')