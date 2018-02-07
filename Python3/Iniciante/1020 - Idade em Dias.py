idade = int(input())
anos = idade // 365
idade %= 365
meses = idade // 30
idade %= 30
dias = idade
print('{} ano(s)'.format(anos))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(dias))
