""" F-string """
x = 12.5678
print(f'{x:.2E}')     # 2exp
print(f'{x:.2}')      # 2sf
print(f'{x:.2f}')     # 2dp

y = 1_000_000         # separator
print(f'{y:,}')
print(f'{y:_}')
print(f'{y=:}')       #  y=...

z = "Hi"
print(f'|{z: ^10}|')  # center
print(f'|{z:*>10}|')  # left
print(f'|{z:#<12}|')  # right

pv = 100; nv = -100
print(f'{pv: }')      # space-align
print(f'{pv:+}')      # +ve sign
print(f'{nv:+}')
