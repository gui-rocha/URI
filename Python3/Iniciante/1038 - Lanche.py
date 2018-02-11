valores = input().split(' ')
codigo = int(valores[0])
quantidade = int(valores[1])
if codigo == 1:
    total = 4 * quantidade
    print('Total: R$ {:.2f}'.format(total))
elif codigo == 2:
    total = 4.5 * quantidade
    print('Total: R$ {:.2f}'.format(total))
elif codigo == 3:
    total = 5 * quantidade
    print('Total: R$ {:.2f}'.format(total))
elif codigo == 4:
    total = 2 * quantidade
    print('Total: R$ {:.2f}'.format(total))
elif codigo == 5:
    total = 1.5 * quantidade
    print('Total: R$ {:.2f}'.format(total))
