import math
T = int(input())

res = []
for _ in range(T):
    DIM = int(input())
    matrix = [list(map(int, input().split())) for _ in range(DIM)]

    # Forward Elimination
    for PIVOT in range(DIM):
        partial_pivot = PIVOT
        for r in range(PIVOT+1, DIM):
            if abs(matrix[r][PIVOT]) > abs(matrix[partial_pivot][PIVOT]):
                partial_pivot = r
        matrix[PIVOT], matrix[partial_pivot] = matrix[partial_pivot], matrix[PIVOT]

        for r in range(PIVOT+1, DIM):
            scale_factor = matrix[r][PIVOT] / matrix[PIVOT][PIVOT]
            for c in range(DIM + 1):
                matrix[r][c] -= scale_factor * matrix[PIVOT][c]

    # Backward Propagation
    ans = [0] * DIM
    for PIVOT in range(DIM - 1, -1, -1):
        total = 0
        for c in range(PIVOT + 1, DIM):
            total += matrix[PIVOT][c] * ans[c]
        ans[PIVOT] = (matrix[PIVOT][DIM] - total) / matrix[PIVOT][PIVOT]
    
    res.append(' '.join(map(lambda a: f'{a:.1f}', ans)))

for i, ans in enumerate(res, start=1):
    print(f'Case #{i}: {ans}')