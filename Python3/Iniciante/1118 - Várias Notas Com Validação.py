soma = cont = opcao = 0
while True:
    n = float(input())
    if 0 <= n <= 10:
        cont += 1
        soma += n
    else:
        print('nota invalida')
    if cont == 2:
        print('media = {:.2f}'.format(soma / 2))
        cont = soma = opcao = 0
        while opcao != 1:
            opcao = int(input('novo calculo (1-sim 2-nao)\n'))
            if opcao == 2:
                break
        if opcao == 2:
            break
