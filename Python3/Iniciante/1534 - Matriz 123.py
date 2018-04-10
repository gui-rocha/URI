while True:
    try:
        N = int(input())
        k = N
        for i in range(1, N+1):
            for j in range(1, N+1):
                if j == k:
                    print(2, end='')
                    k -= 1
                elif i == j:
                    print(1, end='')
                else:
                    print(3, end='')
                if j == N:
                    print()
    except EOFError:
        break
