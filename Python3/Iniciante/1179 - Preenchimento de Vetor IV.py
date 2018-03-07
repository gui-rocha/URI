par = []
impar = []
for i in range(15):
    valor = int(input())
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
    if len(par) == 5:
        for p in range(5):
            print('par[{}] = {}'.format(p, par[p]))
        par = []
    if len(impar) == 5:
        for im in range(5):
            print('impar[{}] = {}'.format(im, impar[im]))
        impar = []
if len(impar) > 0:
    x = 0
    for im in impar:
        print('impar[{}] = {}'.format(x, im))
        x += 1
if len(par) > 0:
    x = 0
    for p in par:
        print('par[{}] = {}'.format(x, p))
        x += 1
