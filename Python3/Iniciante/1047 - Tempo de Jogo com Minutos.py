hInicial, mInicial, hFinal, mFinal = map(int, input().split(' '))
totalHoras = hFinal - hInicial
totalMinutos = mFinal - mInicial

if hInicial == hFinal:
    totalHoras = 24
elif hFinal < hInicial:
    totalHoras = 24 - hInicial + hFinal
if mFinal < mInicial:
    totalMinutos = 60 - mInicial + mFinal
    totalHoras -= 1

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(totalHoras, totalMinutos))
