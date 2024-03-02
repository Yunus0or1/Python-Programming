def mergeSort (array, left, right):
    if left >= right:
        return

    mid = left + (right - left) //2
    mergeSort(array, left, mid)
    mergeSort(array, mid+1, right)

    merge(array, left, mid, right)

def merge(array, left, mid, right):
    leftArr = array[left: mid + 1]
    rightArr = array[mid+1: right + 1]

    print(leftArr, rightArr, left,  mid, right)

    i = j =  0
    k = left

    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] < rightArr[j]:
            array[k] = leftArr[i]
            i = i + 1

        else:
            array[k] = rightArr[j]
            j = j + 1

        k = k + 1

    while i < len(leftArr):
        array[k] = leftArr[i]
        k = k + 1
        i = i + 1

    while j <  len(rightArr):
        array[k] = rightArr[j]
        k = k + 1
        j = j + 1


array = [2, 4, 6, 8, 1, 5, 3]
# array = [2,1]
array = [2,3,1]

mergeSort(array, 0, len(array) -1 )
print(array)
