C = int(input())
T = str(input())
lista = []
soma = 0
for i in range(144):
    X = float(input())
    lista.append(X)
matrix = [lista[i:i+12] for i in range(0, len(lista), 12)]
for i in range(12):
    soma += matrix[i][C]
if T == 'S':
    print('{:.1f}'.format(soma))
elif T == 'M':
    print('{:.1f}'.format(soma / 12))
