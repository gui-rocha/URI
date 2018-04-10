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
    for i in range(N):
        for j in range(N):
            if i == j:
                matriz[i][j] = 1
            elif j <= N:
                matriz[i][j] = matriz[i][j-1] + 1
    k = N
    for i in range(N):
        for j in range(N-k):
            matriz[i][j] = matriz[i-1][j] + 1
        k -= 1
    for i in range(N):
        for j in range(N):
            if matriz[i][j] >= 100 and j == 0 and matriz[i][j+1] < 100:
                print(matriz[i][j], end='  ')
            elif matriz[i][j] > 9 and j == 0 and matriz[i][j+1] < 10:
                print('', matriz[i][j], end='   ')
            elif matriz[i][j] > 9 and j == 0 and matriz[i][j+1] >= 10:
                print('', matriz[i][j], end='  ')
            elif j == N - 1 and N == 1:
                print(' ', matriz[i][j])
            elif j == N - 1:
                print(matriz[i][j])
            elif j == 0:
                print(' ', matriz[i][j], end='   ')
            else:
                if matriz[i][j] >= 9 and matriz[i][j+1] == 100:
                    print(matriz[i][j], end=' ')
                elif matriz[i][j] >= 9 and matriz[i][j+1] > 9:
                    print(matriz[i][j], end='  ')
                else:
                    print(matriz[i][j], end='   ')
    print()
