X = int(input())
Y = int(input())
if X > Y:
    maior = X
    menor = Y
else:
    maior = Y
    menor = X
soma = 0
for i in range(menor+1, maior):
    if i % 2 != 0:
        soma += i
print(soma)
