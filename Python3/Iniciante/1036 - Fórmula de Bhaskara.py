from math import sqrt
valores = str(input()).split(' ')
A = float(valores[0])
B = float(valores[1])
C = float(valores[2])
delta = B ** 2 - (4 * A * C)
if A == 0 or delta < 0:
    print('Impossivel calcular')
else:
    R1 = (-B + sqrt(delta)) / (2 * A)
    R2 = (-B - sqrt(delta)) / (2 * A)
    print('R1 = {:.5f}'.format(R1))
    print('R2 = {:.5f}'.format(R2))
