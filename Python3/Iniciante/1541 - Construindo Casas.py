while True:
    valor = list(map(int, input().split()))
    if valor[0] == 0:
        break
    else:
        A = valor[0]
        B = valor[1]
        C = valor[2]
    print(int(((A * B * 100) / C) ** (1/2)))
