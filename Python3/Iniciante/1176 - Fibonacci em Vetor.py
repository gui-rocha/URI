N = int(input())
for i in range(0, N):
    X = int(input())
    sequencia = 2
    lista = [0, 1]
    while sequencia <= X:
        proximo = lista[sequencia-1] + lista[sequencia-2]
        lista.append(proximo)
        sequencia += 1
    print('Fib({}) = {}'.format(X, lista[X]))
