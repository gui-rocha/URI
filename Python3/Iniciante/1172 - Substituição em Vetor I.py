vetor = []
for i in range(0, 10):
    X = int(input())
    vetor.append(X)
    if X <= 0:
        vetor[i] = 1
    print('X[{}] = {}'.format(i, vetor[i]))
