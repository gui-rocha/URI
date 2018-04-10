C = int(input())
for i in range(C):
    nome, newtons = map(str, input().split())
    forca = int(newtons)
    if nome == 'Thor' and forca > 0:
        print('Y')
    else:
        print('N')
