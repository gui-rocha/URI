X = int(input())
Z = int(input())
soma = cont = 0
while X >= Z:
    Z = int(input())
while soma < Z:
    soma += X
    X += 1
    cont += 1
print(cont)
