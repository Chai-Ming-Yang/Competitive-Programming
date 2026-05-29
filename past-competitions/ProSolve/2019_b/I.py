T = int(input())

for _ in range(T):
    m = int(input())
    
    k = (m - 2)//2
    h = 4*k + (m - 2*k)
    
    print(f'{h//24}d{h%24}h')
