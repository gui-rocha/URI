salario = float(input())
if 0 <= salario <= 2000.00:
    print('Isento')
else:
    if 2000 < salario <= 3000.00:
        imposto = 0.08 * (salario - 2000)
        print('R$ {:.2f}'.format(imposto))
    elif 3000 < salario <= 4500.00:
        imposto = (0.08 * 1000) + (0.18 * (salario - 3000))
        print('R$ {:.2f}'.format(imposto))
    elif salario > 4500.00:
        imposto = (0.08 * 1000) + (0.18 * 1500) + (0.28 * (salario - 4500))
        print('R$ {:.2f}'.format(imposto))
