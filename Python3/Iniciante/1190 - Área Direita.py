T = str(input())
lista = []
soma = cont = 0
k = 11
for i in range(144):
    X = float(input())
    lista.append(X)
matrix = [lista[i:i+12] for i in range(0, len(lista), 12)]
for i in range(1, 11):
    for j in range(k, 12):
        soma += matrix[i][j]
        cont += 1
    if i > 5:
        k += 1
    elif i == 5:
        k = k
    else:
        k -= 1
if T == 'S':
    print('{:.1f}'.format(soma))
elif T == 'M':
    print('{:.1f}'.format(soma / cont))
