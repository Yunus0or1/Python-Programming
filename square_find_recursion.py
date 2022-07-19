def sqrt(n):
    return sqrt_helper(n, 1, n)


def sqrt_helper(n,min,max):
    if max< min :
        return -1


    guess = int((min + max ) /2)



    if guess * guess == n :
         return guess

    elif guess * guess < n:
        print('L : ',n, guess , max)
        return sqrt_helper(n, guess +1, max)

    else:
        print('H : ',n, min, guess)
        return sqrt_helper(n, min, guess -1 )


print(sqrt(2254))