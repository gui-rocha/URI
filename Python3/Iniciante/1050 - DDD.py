codigo = int(input())
listaDDD = [61, 71, 11, 21, 32, 19, 27, 31]
listaCidade = ['Brasilia', 'Salvador', 'Sao Paulo', 'Rio de Janeiro', 'Juiz de Fora', 'Campinas', 'Vitoria', 'Belo Horizonte']
cont = 0
for i in range(0, 8):
    if codigo == listaDDD[i]:
        cont = 1
        print(listaCidade[i])
if cont == 0:
    print('DDD nao cadastrado')
