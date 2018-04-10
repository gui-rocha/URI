T = str(input())
lista = []
soma = 0
k = 12
for i in range(144):
    X = float(input())
    lista.append(X)
matrix = [lista[i:i+12] for i in range(0, len(lista), 12)]
for i in range(12):
    for j in range(k, 12):
        soma += matrix[i][j]
    k -= 1
if T == 'S':
    print('{:.1f}'.format(soma))
elif T == 'M':
    print('{:.1f}'.format(soma / 66))
