def countSort(array):
    max = 0

    for i in range(len(array)):
        if array[i] > max:
            max = array[i]

    countArray = [0] * max+1

    for i in range (0, len(array)):
        countArray[array[i]] = countArray[array[i]] + 1

    print(countArray)
    for i in range (1, len(countArray)):
        countArray[i] = countArray[i] + countArray[i -1]

    print(countArray)

    newArr = [0 for x in range(len(array))]
    # for i in range (0, len(array)):
    #     position = countArray[array[i]]
    #     newArr[position - 1] = array[i]
    #
    #     countArray[array[i]] = countArray[array[i]] + 1

    return newArr

array = [3,1,2,0, 6 ,9,9]

print(countSort(array))


