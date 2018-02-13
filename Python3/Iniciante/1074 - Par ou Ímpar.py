N = int(input())
lista = []
for i in range(0, N):
    lista.append(int(input()))
for X in lista:
    if X == 0:
        print('NULL')
    elif X % 2 == 0 and X > 0:
        print('EVEN POSITIVE')
    elif X % 2 == 0 and X < 0:
        print('EVEN NEGATIVE')
    elif X % 2 != 0 and X > 0:
        print('ODD POSITIVE')
    elif X % 2 != 0 and X < 0:
        print('ODD NEGATIVE')
