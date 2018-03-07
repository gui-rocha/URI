L = int(input())
T = str(input())
lista = []
for i in range(144):
    X = float(input())
    lista.append(X)
matrix = [lista[i:i+12] for i in range(0, len(lista), 12)]
if T == 'S':
    print('{:.1f}'.format(sum(matrix[L])))
elif T == 'M':
    print('{:.1f}'.format(sum((matrix[L])) / 12))
