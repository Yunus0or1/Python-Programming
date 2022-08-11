def merge(array, p, q, r):

    n1 = q - p + 1
    n2 = r - q

    L = []
    R = []

    for i in range(n1):
        L.append(array[i + p])

    for j in range(n2):
        R.append(array[q + 1 + j])

    i = j = 0
    k = p

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i = i + 1
            k = k + 1

        elif R[j] < L[i]:
            array[k] = R[j]
            j = j + 1
            k = k + 1

    while i < n1:
        array[k] = L[i]
        i = i + 1
        k = k + 1

    while j < n2:
        array[k] = R[j]
        j = j + 1
        k = k + 1


def mergeSort(nums, l, r,):
    if l >= r:
        return

    mid = int((l + r) / 2)

    mergeSort(nums, l, mid)
    mergeSort(nums, mid + 1, r)
    merge(nums, l, mid, r)

    return nums


nums = [ 9,3, 8, 7, 1, 1]
print(mergeSort(nums, 0, len(nums)-1))
