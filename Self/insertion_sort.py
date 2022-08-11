def insertionSort(nums):
    for i in range(1, len(nums)):
        item = nums[i]
        j = i - 1

        while j>=0 and item < nums[j]:
            nums[j+1] = nums[j]
            j = j -1


        nums[j + 1] = item

    return nums


nums = [ 3, 9, 8, 7,1,1]
print(insertionSort(nums))
