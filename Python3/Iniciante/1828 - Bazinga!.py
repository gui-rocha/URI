N = int(input())
for i in range(N):
    sheldon, raj = map(str, input().split())
    if sheldon == 'tesoura' and raj == 'papel':
        print('Caso #{}: Bazinga!'.format(i + 1))
    elif sheldon == 'papel' and raj == 'tesoura':
        print('Caso #{}: Raj trapaceou!'.format(i + 1))
    elif sheldon == 'papel' and raj == 'pedra':
        print('Caso #{}: Bazinga!'.format(i + 1))
    elif sheldon == 'pedra' and raj == 'papel':
        print('Caso #{}: Raj trapaceou!'.format(i + 1))
    elif sheldon == 'pedra' and raj == 'lagarto':
        print('Caso #{}: Bazinga!'.format(i + 1))
    elif sheldon == 'lagarto' and raj == 'pedra':
        print('Caso #{}: Raj trapaceou!'.format(i + 1))
    elif sheldon == 'lagarto' and raj == 'Spock':
        print('Caso #{}: Bazinga!'.format(i + 1))
    elif sheldon == 'Spock' and raj == 'lagarto':
        print('Caso #{}: Raj trapaceou!'.format(i + 1))
    elif sheldon == 'Spock' and raj == 'tesoura':
        print('Caso #{}: Bazinga!'.format(i + 1))
    elif sheldon == 'tesoura' and raj == 'Spock':
        print('Caso #{}: Raj trapaceou!'.format(i + 1))
    elif sheldon == 'tesoura' and raj == 'lagarto':
        print('Caso #{}: Bazinga!'.format(i + 1))
    elif sheldon == 'lagarto' and raj == 'tesoura':
        print('Caso #{}: Raj trapaceou!'.format(i + 1))
    elif sheldon == 'lagarto' and raj == 'papel':
        print('Caso #{}: Bazinga!'.format(i + 1))
    elif sheldon == 'papel' and raj == 'lagarto':
        print('Caso #{}: Raj trapaceou!'.format(i + 1))
    elif sheldon == 'papel' and raj == 'Spock':
        print('Caso #{}: Bazinga!'.format(i + 1))
    elif sheldon == 'Spock' and raj == 'papel':
        print('Caso #{}: Raj trapaceou!'.format(i + 1))
    elif sheldon == 'Spock' and raj == 'pedra':
        print('Caso #{}: Bazinga!'.format(i + 1))
    elif sheldon == 'pedra' and raj == 'Spock':
        print('Caso #{}: Raj trapaceou!'.format(i + 1))
    elif sheldon == 'pedra' and raj == 'tesoura':
        print('Caso #{}: Bazinga!'.format(i + 1))
    elif sheldon == 'tesoura' and raj == 'pedra':
        print('Caso #{}: Raj trapaceou!'.format(i + 1))
    elif sheldon == raj:
        print('Caso #{}: De novo!'.format(i + 1))
