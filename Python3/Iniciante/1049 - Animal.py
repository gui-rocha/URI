A = str(input())
B = str(input())
C = str(input())
if A == 'vertebrado':
    if B == 'ave':
        if C == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if C == 'onivoro':
            print('homem')
        else:
            print('vaca')
elif A == 'invertebrado':
    if B == 'inseto':
        if C == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if C == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')
