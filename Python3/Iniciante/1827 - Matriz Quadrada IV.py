while True:
    try:
        N = int(input())
        matriz = []
        for i in range(N):
            tmp = []
            for j in range(N):
                tmp.append(0)
            matriz.append(tmp[:])
        k = N - 1
        for i in range(N):
            for j in range(N):
                if i == (N - 1) / 2 and j == (N - 1) / 2:
                    matriz[i][j] = 4
                elif (int(N / 3) <= i <= (N - int(N / 3) - 1)) and (int(N / 3) <= j <= (N - int(N / 3) - 1)):
                    matriz[i][j] = 1
                elif i == j and (i < int(N / 3) or i > i - int(N / 3)):
                    matriz[i][j] = 2
                elif j == k and (i < int(N / 3) or i > i - int(N / 3)):
                    matriz[i][j] = 3
            k -= 1

        for i in range(N):
            for j in range(N):
                if j == N - 1:
                    print(matriz[i][j])
                else:
                    print(matriz[i][j], end='')
        print()
    except EOFError:
        break
