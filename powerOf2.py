def powerOf2(n):
    if n < 1:
        return 0
    if n == 1:
        return 1

    else:
        prev = powerOf2(int(n / 2))
        if prev == 1: print(prev)
        curr = prev * 2

        print(curr)
        return curr


powerOf2(50)
