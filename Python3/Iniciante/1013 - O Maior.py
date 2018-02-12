A, B, C = map(int,input().split(' '))
maiorAB = int((A + B + abs(A - B)) / 2)
maior = int((maiorAB + C + abs(maiorAB - C)) / 2)
print('{} eh o maior'.format(maior))
