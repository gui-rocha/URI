t1, t2,  t3 = map(int, input().split())
if t2 > t1:
    if t3 <= t2:
        print(':(')
    elif t2 - t1 > t3 - t2:
        print(':(')
    elif t3 - t2 >= t2 - t1:
        print(':)')
elif t2 < t1:
    if t3 >= t2:
        print(':)')
    elif t1 - t2 > t2 - t3:
        print(':)')
    elif t1 - t2 <= t2 - t3:
        print(':(')
elif t1 == t2:
    if t2 < t3:
        print(':)')
    elif t2 >= t3:
        print(':(')
