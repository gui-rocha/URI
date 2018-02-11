valor = float(input())
n = valor #Notas
m = round(valor % 1, 2) #Moedas
dinheiro = [100, 50, 20, 10, 5, 2, 0.50, 0.25, 0.10, 0.05, 0.01]
print('NOTAS:')
for i in range(0, 6):
    qn = n // dinheiro[i]
    n %= dinheiro[i]
    print('{:.0f} nota(s) de R$ {:.2f}'.format(qn, dinheiro[i]))
print('MOEDAS:')
print('{:.0f} moeda(s) de R$ 1.00'.format(n // 1))
for i in range(6, 10):
    qm = m // dinheiro[i]
    m %= dinheiro[i]
    m = round(m, 2)
    print('{:.0f} moeda(s) de R$ {:.2f}'.format(qm, dinheiro[i]))
print('{:.0f} moeda(s) de R$ 0.01'.format(m / 0.01))

''' OU 
valor = float(input())
n = valor
cem = n // 100
n %= 100
cinquenta = n // 50
n %= 50
vinte = n // 20
n %= 20
dez = n // 10
n %= 10
cinco = n // 5
n %= 5
dois = n // 2
n %= 2
um = n // 1
m = valor % 1
m = round(m, 2)
cinquentac = m // 0.50
m %= 0.50
m = round(m, 2)
vintecincoc = m // 0.25
m %= 0.25
m = round(m, 2)
dezc = m // 0.10
m %= 0.10
m = round(m, 2)
cincoc = m // 0.05
m %= 0.05
m = round(m, 2)
umc = m / 0.01
print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(int(cem)))
print('{} nota(s) de R$ 50.00'.format(int(cinquenta)))
print('{} nota(s) de R$ 20.00'.format(int(vinte)))
print('{} nota(s) de R$ 10.00'.format(int(dez)))
print('{} nota(s) de R$ 5.00'.format(int(cinco)))
print('{} nota(s) de R$ 2.00'.format(int(dois)))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(int(um)))
print('{} moeda(s) de R$ 0.50'.format(int(cinquentac)))
print('{} moeda(s) de R$ 0.25'.format(int(vintecincoc)))
print('{} moeda(s) de R$ 0.10'.format(int(dezc)))
print('{} moeda(s) de R$ 0.05'.format(int(cincoc)))
print('{} moeda(s) de R$ 0.01'.format(int(umc)))'''
