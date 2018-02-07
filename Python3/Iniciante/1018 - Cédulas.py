valor = int(input())
m = valor
cem = m // 100
m %= 100
cinquenta = m // 50
m %= 50
vinte = m // 20
m %= 20
dez = m // 10
m %= 10
cinco = m // 5
m %= 5
dois = m // 2
m %= 2
um = m // 1
m %= 1
print(valor)
print('{} nota(s) de R$ 100,00'.format(cem))
print('{} nota(s) de R$ 50,00'.format(cinquenta))
print('{} nota(s) de R$ 20,00'.format(vinte))
print('{} nota(s) de R$ 10,00'.format(dez))
print('{} nota(s) de R$ 5,00'.format(cinco))
print('{} nota(s) de R$ 2,00'.format(dois))
print('{} nota(s) de R$ 1,00'.format(um))
