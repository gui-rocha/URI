n1, n2, n3, n4 = map(float, input().split(' '))
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
print('Media: {:.1f}'.format(media))
if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    notaExame = float(input())
    print('Nota do exame: {:.1f}'.format(notaExame))
    novaMedia = (media + notaExame) / 2
    if novaMedia >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(novaMedia))
