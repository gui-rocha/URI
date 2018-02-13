cont = 0
soma = 0
for i in range(0, 6):
    valor = float(input())
    if valor > 0:
        cont += 1
        soma += valor
media = soma / cont
print('{} valores positivos'.format(cont))
print('{:.1f}'.format(media))
