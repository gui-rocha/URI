n = int(input())
for i in range(0, n):
    A, B, G1, G2 = map(float, input().split(' '))
    A = int(A)
    B = int(B)
    anos = 1
    while True:
        A += int(A * (G1 / 100))
        B += int(B * (G2 / 100))
        if anos > 100 or A > B:
            break
        anos += 1
    if anos > 100:
        print('Mais de 1 seculo.')
    else:
        print('{} anos.'.format(anos))
