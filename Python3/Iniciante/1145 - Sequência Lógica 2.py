x, y = map(int, input().split(' '))
k = i = 1
while i < y:
    for j in range(0, x):
        if j != x-1:
            print(k, end=' ')
        else:
            print(k)
        k += 1
        if k == y+1:
            i += 1
            break
        i += 1
