contAlcool = contGasolina = contDiesel = 0
while True:
    opcao = int(input())
    if 1 > opcao > 4:
        opcao = int(input())
    else:
        if opcao == 1:
            contAlcool += 1
        elif opcao == 2:
            contGasolina += 1
        elif opcao == 3:
            contDiesel += 1
        elif opcao == 4:
            break
print('MUITO OBRIGADO')
print('Alcool: {}'.format(contAlcool))
print('Gasolina: {}'.format(contGasolina))
print('Diesel: {}'.format(contDiesel))
