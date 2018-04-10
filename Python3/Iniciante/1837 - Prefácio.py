a, b = map(int, input().split())
if b < 0:
    b *= -1
    print((a // b) * -1, a % b)
else:
    print(a // b, a % b)
