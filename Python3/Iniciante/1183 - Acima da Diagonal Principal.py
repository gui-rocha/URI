T = str(input())
lista = []
soma = 0
k = p = 12
for i in range(144):
    X = float(input())
    lista.append(X)
matrix = [lista[i:i+12] for i in range(0, len(lista), 12)]
for i in range(12):
    for j in range(12 - p):
        soma += matrix[i][j]
    p -= 1
if T == 'S':
    print('{:.1f}'.format(soma))
elif T == 'M':
    print('{:.1f}'.format(soma / 66))
