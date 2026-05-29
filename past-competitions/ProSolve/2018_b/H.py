N = int(input())

X, Y = [], []
for _ in range(N):
    nx, ny = map(float, input().split())
    X.append(nx); Y.append(ny)

XBAR, YBAR = sum(X)/N, sum(Y)/N

Sxy, Sxx = 0, 0
for x, y in zip(X, Y):
    x_xbar, y_ybar = x - XBAR, y - YBAR
    Sxy += x_xbar * y_ybar
    Sxx += x_xbar * x_xbar

beta = Sxy / Sxx
alpha = YBAR - beta * XBAR

print(f'{beta:.4f} {alpha:.4f}')

Q = int(input())
for _ in range(Q):
    x = float(input())
    print(f'{alpha + beta * x:.4f}')