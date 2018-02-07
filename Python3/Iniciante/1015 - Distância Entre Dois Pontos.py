from math import sqrt
p1 = input().split(' ')
p2 = input().split(' ')
x1 = float(p1[0])
y1 = float(p1[1])
x2 = float(p2[0])
y2 = float(p2[1])
distancia = sqrt((x2 - x1)**2 + (y2 - y1)**2)
print('{:.4f}'.format(distancia))
