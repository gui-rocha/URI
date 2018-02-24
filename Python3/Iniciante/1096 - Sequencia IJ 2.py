i = 1
j = 7
while i <= 9:
    for k in range(0, 3):
        print('I={} J={}'.format(i, j))
        j -= 1
        if k == 2:
            break
    i += 2
    j = 7
