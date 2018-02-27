N = int(input())
soma = 0
for i in range(0, N):
    X, Y = map(int, input().split(' '))
    if X % 2 != 0:
        for k in range(X, X+Y):
            soma += X
            X += 2
        print(soma)
        soma = 0
    else:
        for k in range(X+1, X+Y+1):
            soma += X+1
            X += 2
        print(soma)
        soma = 0
