contPar = 0
contImpar = 0
contPositivo = 0
contNegativo = 0
for i in range(0, 5):
    valor = int(input())
    if valor % 2 == 0:
        contPar += 1
    elif valor % 2 != 0:
        contImpar += 1
    if valor > 0:
        contPositivo += 1
    if valor < 0:
        contNegativo += 1
print('{} valor(es) par(es)'.format(contPar))
print('{} valor(es) impar(es)'.format(contImpar))
print('{} valor(es) positivo(s)'.format(contPositivo))
print('{} valor(es) negativo(s)'.format(contNegativo))
