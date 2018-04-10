while True:
    try:
        L = int(input())
        lista = list(map(int, input().split()))
        if max(lista) < 10:
            print(1)
        elif 10 <= max(lista) < 20:
            print(2)
        else:
            print(3)
    except EOFError:
        break
