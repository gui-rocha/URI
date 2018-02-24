n = int(input())
total = totalC = totalR = totalS = 0
for i in range(0, n):
    q, t = map(str, input().split(' '))
    q = int(q)
    total += q
    if t == 'C':
        totalC += q
    if t == 'R':
        totalR += q
    if t == 'S':
        totalS += q
    percC = (totalC / total) * 100
    percR = (totalR / total) * 100
    percS = (totalS / total) * 100
print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(totalC))
print('Total de ratos: {}'.format(totalR))
print('Total de sapos: {}'.format(totalS))
print('Percentual de coelhos: {:.2f} %'.format(percC))
print('Percentual de ratos: {:.2f} %'.format(percR))
print('Percentual de sapos: {:.2f} %'.format(percS))
