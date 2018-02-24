i = 0
j = 1
while i <= 2:
    for k in range(0, 3):
        if i == 0 or j == 1 or j == 2 or j == 3 or j == 4 or j == 5:
            print('I={:.0f} J={:.0f}'.format(i, j))
        else:
            print('I={:.1f} J={:.1f}'.format(i, j))
        j += 1
        if k == 2:
            break
    i += 0.2
    j = 1 + i
