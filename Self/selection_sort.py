def selectionSort(nums):
    for i in range(0, len(nums)):
        minIndex = i

        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minIndex]:
                minIndex = j

        temp = nums[i]
        nums[i] = nums[minIndex]
        nums[minIndex] = temp

    return nums


nums = [ 3, 9, 8, 7,1,1]
print(selectionSort(nums))
