import math
N, B = map(int, input().split())

print(math.ceil(sum(list(map(int, input().split()))) / float(B)))