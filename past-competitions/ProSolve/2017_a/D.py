frame = list(map(int, input().split()))
round = 0
res = 0
for _ in range(10):
    if frame[round] == 10:
        res += sum(frame[round:round + 3])
        round += 1
        continue
    
    res += sum(frame[round:round+2])
    if frame[round] + frame[round + 1] == 10:
        res += frame[round + 2]
    round += 2

print(res)