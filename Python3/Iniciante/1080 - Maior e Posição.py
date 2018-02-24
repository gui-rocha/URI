maior = pos = 0
for i in range(1, 101):
    n = int(input())
    if i == 1:
        maior = n
        pos = i
    elif n > maior:
        maior = n
        pos = i
print(maior)
print(pos)
