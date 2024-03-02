def poweraOfb(a, b):
    if b <0:
        return 0
    if b == 0:
        return 1
    else:
        return a * poweraOfb(a, b - 1)


print(poweraOfb(3, 2))
