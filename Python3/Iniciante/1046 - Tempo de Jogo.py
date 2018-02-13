inicial, final = map(int, input().split(' '))
if final < inicial:
    duracao = 24 - inicial + final
elif inicial == final:
    duracao = 24
else:
    duracao = final - inicial
print('O JOGO DUROU {} HORA(S)'.format(duracao))
