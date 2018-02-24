cont = soma = 0
while True:
    n = float(input())
    if 0 <= n <= 10:
        cont += 1
        soma += n
    else:
        print('nota invalida')
    if cont == 2:
        break
print('media = {:.2f}'.format(soma / 2))
