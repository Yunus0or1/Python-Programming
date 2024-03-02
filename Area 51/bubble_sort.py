def bubbleSort(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            print(nums[i], nums[j])
            if nums[i] > nums[j]:
                temp= nums[i]
                nums[i] = nums[j]
                nums[j] = temp



    return nums

nums = [3,9,8,72,3,4,25,6,7]
print(bubbleSort(nums))