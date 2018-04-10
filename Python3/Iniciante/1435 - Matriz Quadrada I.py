while True:
    N = int(input())
    if N == 0:
        break
    matriz = []
    valor = 1
    for i in range(N):
       tmp = []
       for j in range(N):
           tmp.append(1)
       matriz.append(tmp[:])

    while valor < N-1:
        for i in range(N - valor * 2):
            for j in range(N - valor * 2):
                if j < N - valor - 1 and i < N - valor - 1:
                    matriz[i+valor][j+valor] = valor + 1
        valor += 1

    for i in range(N):
        for j in range(N):
            if j == N - 1 and N == 1:
                print(' ', matriz[i][j])
            elif j == N - 1:
                print(matriz[i][j])
            elif j == 0:
                print(' ', matriz[i][j], end='   ')
            else:
                if matriz[i][j] >= 9 and matriz[i][j+1] > 9:
                    print(matriz[i][j], end='  ')
                else:
                    print(matriz[i][j], end='   ')

    print()
