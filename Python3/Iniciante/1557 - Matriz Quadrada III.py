while True:
    N = int(input())
    if N == 0:
        break
    matriz = []
    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append(1)
        matriz.append(tmp[:])
    k = 0
    for i in range(N):
        for j in range(N):
            matriz[i][j] = 2 ** (k + j)
        k += 1

    tam = len(str(matriz[-1][-1]))
    for i in range(N):
        for j in range(N):
            if N <= 2 and j == 0:
                if N == 1:
                    print(matriz[i][j])
                else:
                    print(matriz[i][j], end='')
            elif j == 0 and N > 2:
                print(' ' * (tam - len(str(matriz[i][j]))-1), matriz[i][j], end='')
            elif j == (N - 1):
                print(' ' * (tam - len(str(matriz[i][j]))), matriz[i][j])
            else:
                print(' ' * (tam - len(str(matriz[i][j]))), matriz[i][j], end='')
    print()
