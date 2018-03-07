T = int(input())
j = k = 0
while True:
    if j >= 1000:
        break
    if k == T:
        k = 0
    print('N[{}] = {}'.format(j, k))
    k += 1
    j += 1
