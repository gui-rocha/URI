S = 0
k = 1
for i in range(1, 21):
    S += (k/2 ** (i-1))
    k += 2
print('{:.2f}'.format(S))
