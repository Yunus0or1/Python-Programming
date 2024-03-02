def partition(nums, l, r):
    pivot = nums[r]
    init = l

    for i in range(l, r):
        if nums[i] < pivot:
            temp = nums[i]
            nums[i] = nums[init]
            nums[init] = temp

            init = init + 1

    nums[init], nums[r] = nums[r], nums[init]

    return init


def quickSort(nums, l, r):
    if l>=r:
        return

    paritionIndex = partition(nums, l, r)
    quickSort(nums,0, paritionIndex-1)
    quickSort(nums,paritionIndex + 1, r)

    return nums


nums = [3, 9, 8, 7, 2, 4, 5,1,1]
print(quickSort(nums, 0, len(nums) - 1))
