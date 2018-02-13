N = int(input())
lista = []
contIn = 0
contOut = 0
for i in range(0, N):
    lista.append(int(input()))
for i in range(0, len(lista)):
    if 10 <= lista[i] <= 20:
        contIn += 1
    else:
        contOut += 1
print('{} in'.format(contIn))
print('{} out'.format(contOut))
