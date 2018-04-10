T = str(input())
lista = []
soma = cont = 0
inicio, fim = 1, 11
for i in range(144):
    X = float(input())
    lista.append(X)
matrix = [lista[i:i+12] for i in range(0, len(lista), 12)]
for i in range(6):
    for j in range(inicio, fim):
        soma += matrix[i][j]
        cont += 1
    inicio += 1
    fim -= 1
if T == 'S':
    print('{:.1f}'.format(soma))
elif T == 'M':
    print('{:.1f}'.format(soma / cont))
