
def pivotFind(array, low, high):
    pivot = high
    i = low

    for j in range(low,high):
        if array[j] <= array[pivot]:
            array[i], array[j] = array[j], array[i]
            i = i + 1

    array[i], array[pivot] = array[pivot], array[i]
    return i

def quickSort(array, low, high):
    if low > high:
        return

    pi = pivotFind(array, low, high)

    quickSort(array, low, pi -1)
    quickSort(array, pi + 1, high)

array = [2,4,6,8,1,5,3]
array = [1,1,1,1,1,1,3]
array = [2,1]
quickSort(array, 0 , len(array) - 1)
print(array)

