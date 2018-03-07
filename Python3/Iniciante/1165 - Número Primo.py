N = int(input())
for i in range(0, N):
    cont = 0
    X = int(input())
    for k in range(1, X+1):
        if X % k == 0:
            cont += 1
    if cont == 2:
        print('{} eh primo'.format(X))
    else:
        print('{} nao eh primo'.format(X))
