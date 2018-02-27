soma = cont = 0
while True:
    N = int(input())
    if N < 0:
        break
    else:
        soma += N
        cont += 1
print('{:.2f}'.format(soma / cont))
