# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
from decimal import *

d = input("Введите число d: ")
pi = 3
flag = True
for i in range(0, 1000000, 2):
    if flag:
        pi += Decimal(4/((i + 2) * (i + 3) * (i + 4)))
        flag = False
    elif not flag:
        pi -= Decimal(4/((i + 2) * (i + 3) * (i + 4)))
        flag = True

print(round(pi, len(d[d.index('.') + 1: ])))    
    