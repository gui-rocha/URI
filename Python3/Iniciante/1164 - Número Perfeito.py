N = int(input())
for i in range(0, N):
    soma = 0
    X = int(input())
    for k in range(1, X):
        if X % k == 0:
            soma += k
    if soma == X:
        print('{} eh perfeito'.format(X))
    else:
        print('{} nao eh perfeito'.format(X))
