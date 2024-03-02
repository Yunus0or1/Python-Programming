def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[i]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)
    for x in range(n // 2 - 1, -1, -1):
        heapify(arr, n, x)

    for x in range(n - 1, 0, -1):
        arr[x], arr[0] = arr[0], arr[x]
        heapify(arr, x, 0)


array = [5, 7, 1, 20, 30]

heapSort(array)
print(array)


