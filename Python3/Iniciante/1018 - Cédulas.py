valor = int(input())
lista = [100, 50, 20, 10, 5, 2, 1]
m = valor
print(valor)
for i in range(0, 7):
    quantidadeNotas = m // lista[i]
    m %= lista[i]
    print('{} nota(s) de R$ {},00'.format(quantidadeNotas, lista[i]))
