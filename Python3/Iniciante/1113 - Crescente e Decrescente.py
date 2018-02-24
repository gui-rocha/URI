X = Y = 0
while True:
    X, Y = map(int, input().split(' '))
    if X < Y:
        print('Crescente')
    elif X > Y:
        print('Decrescente')
    else:
        break
