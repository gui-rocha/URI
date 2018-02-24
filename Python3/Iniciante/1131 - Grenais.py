opcao = contGrenais = contInter = contGremio = contEmpate = 0
while True:
        inter, gremio = map(int, input().split(' '))
        contGrenais += 1
        if inter > gremio:
            contInter += 1
        elif gremio > inter:
            contGremio += 1
        elif gremio == inter:
            contEmpate += 1
        opcao = int(input('Novo grenal (1-sim 2-nao)\n'))
        if opcao == 2:
            break
print('{} grenais'.format(contGrenais))
print('Inter:{}'.format(contInter))
print('Gremio:{}'.format(contGremio))
print('Empates:{}'.format(contEmpate))
if contInter > contGremio:
    print('Inter venceu mais')
elif contInter < contGremio:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')
