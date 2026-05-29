a = list(map(int, input().split()))
N = len(a)
print(f'Mean : {sum(a)/N:.2f}')
print(f'Median : {a[N//2]:.2f}')