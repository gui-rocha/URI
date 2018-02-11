inicio = input().split(' ')
horarioi = input().split(' ')
fim = input().split(' ')
horariof = input().split(' ')
diai = int(inicio[1])
horai = int(horarioi[0])
minutoi = int(horarioi[2])
segundoi = int(horarioi[4])
diaf = int(fim[1])
horaf = int(horariof[0])
minutof = int(horariof[2])
segundof = int(horariof[4])

totalDias = diaf - diai
totalHoras = horaf - horai
if totalHoras < 0:
    totalHoras = 24 + totalHoras
    totalDias = totalDias - 1

totalMinutos = minutof - minutoi
if totalMinutos < 0:
    totalMinutos = 60 + totalMinutos
    totalHoras = totalHoras - 1

totalSegundos = segundof - segundoi
if totalSegundos < 0:
    totalSegundos = 60 + totalSegundos
    totalMinutos = totalMinutos - 1

if totalDias <= 0:
    totalDias = 0

print('{} dia(s)'.format(totalDias))
print('{} hora(s)'.format(totalHoras))
print('{} minuto(s)'.format(totalMinutos))
print('{} segundo(s)'.format(totalSegundos))
