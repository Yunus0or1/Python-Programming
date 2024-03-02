def countSort(nums, sortingBit):
    n = len(nums)
    result = [0] * 10
    countArray = [0] * 10

    # [23, 25, 11, 10, 28, 88, 78, 99, 55]
    # [1, 1, 0, 1, 0, 2, 0, 0, 3, 1]
    for i in range(len(nums)):
        sortingNumber = nums[i] // sortingBit
        sortingNumber = sortingNumber % 10
        countArray[sortingNumber] = countArray[sortingNumber]  + 1

    for i in range(1, len(countArray)):
        countArray[i] = countArray[i] + countArray[i-1]

    # Reducing 1 to get the correct position
    for i in range(len(countArray)):
        countArray[i] = countArray[i] - 1

    for i in range(len(nums)-1, -1, -1):
        sortingNumber = nums[i] // sortingBit
        sortingNumber = sortingNumber % 10

        actualPosition = countArray[sortingNumber]
        result[actualPosition] = nums[i]

        countArray[sortingNumber] = countArray[sortingNumber] -1

    for i in range(0, len(nums)):
        nums[i] = result[i]


def radixSort(nums):
    max = -1

    for i in range(len(nums)):
        if nums[i] > max:
            max = nums[i]

    sortingPosition = 1 # Starting from the right most bit
    while max > 0:
        countSort(nums,sortingPosition)
        sortingPosition = sortingPosition * 10
        max = max //10



nums = [23, 25, 11, 10, 28, 88, 78, 99, 55]
radixSort(nums)
print(nums)
