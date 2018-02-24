soma = 0
while True:
    M, N = map(int, input().split(' '))
    if M <= 0 or N <= 0:
        break
    if M > N:
        maior = M
        menor = N
    else:
        maior = N
        menor = M
    for i in range(menor, maior+1):
        print(i, end=' ')
        soma += i
    print('Sum={}'.format(soma))
    soma = 0
