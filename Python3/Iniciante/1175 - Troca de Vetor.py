lista = []
lista2 = []
k = 0
for i in range(20):
    N = int(input())
    lista.append(N)

for i in range(len(lista) - 1, -1, -1):
    lista2.append(lista[i])
    print('N[{}] = {}'.format(k, lista2[k]))
    k += 1
