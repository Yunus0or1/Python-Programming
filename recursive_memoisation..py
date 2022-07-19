def fib(n, memo):
    if n == 0:
        return 0

    if n == 1:
        return 1

    if memo[n] != None:
        return memo[n]

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    print(memo)
    return memo[n]


def allFib(n):
    memo = [None] * (n+1)
    for i in range(0, n):
        print(str(i) + ' ' + str(fib(n, memo)))


allFib(3)
