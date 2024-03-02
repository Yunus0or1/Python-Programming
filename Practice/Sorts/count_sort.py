def countSort(nums):
    max = -1

    for i in range(len(nums)):
        if nums[i] > max:
            max = nums[i]

    array = [0] * (max + 1)

    for i in range(len(nums)):
        array[nums[i]] = array[nums[i]] + 1

    for i in range(1, len(array)):
        array[i] = array[i] + array[i - 1]

    result = [0] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        position = array[nums[i]] - 1
        result[position] = nums[i]
        array[nums[i]] = array[nums[i]] - 1

    return result


nums = [2, 1, 5, 1, 2, 55]
print(countSort(nums))
