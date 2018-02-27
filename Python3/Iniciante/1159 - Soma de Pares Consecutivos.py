cont = soma = 0
while True:
    X = int(input())
    if X == 0:
        break
    else:
        while cont < 5:
            if X % 2 == 0:
                soma += X
                cont += 1
            X += 1
        print(soma)
        soma = 0
        cont = 0
