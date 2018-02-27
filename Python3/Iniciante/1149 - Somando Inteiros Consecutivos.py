lista = list(map(int, input().split()))
A = 'P'
N = soma = 0
for i in lista:
    if A == 'P':
        A = i
    else:
        if i > 0:
            N = i
            break
for i in range(N):
    soma += A
    A += 1
print(soma)
