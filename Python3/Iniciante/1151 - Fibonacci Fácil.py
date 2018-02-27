N = int(input())
sequencia = 2
lista = [0, 1]
while sequencia < N:
    proximo = lista[sequencia-1] + lista[sequencia-2]
    lista.append(proximo)
    sequencia += 1
for i in range(0, N):
    if i == N - 1:
        print('{}'.format(lista[i]))
    else:
        print(lista[i], end=' ')
