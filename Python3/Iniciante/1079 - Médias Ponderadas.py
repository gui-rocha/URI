n = int(input())
for i in range(0, n):
    a, b, c = map(float, input().split(' '))
    media = ((2 * a) + (3 * b) + (5 * c)) / 10
    print('{:.1f}'.format(media))
