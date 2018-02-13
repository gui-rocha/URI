salario = float(input())
if salario <= 400:
    percentual = 0.15
elif 400 < salario <= 800:
    percentual = 0.12
elif 800 < salario <= 1200:
    percentual = 0.10
elif 1200 < salario <= 2000:
    percentual = 0.07
elif salario > 2000:
    percentual = 0.04
reajuste = salario * percentual
novoSalario = salario + reajuste
print('Novo salario: {:.2f}'.format(novoSalario))
print('Reajuste ganho: {:.2f}'.format(reajuste))
print('Em percentual: {:.0f} %'.format(percentual * 100))
