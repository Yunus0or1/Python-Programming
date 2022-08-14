def binarySearch(nums, k):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = int((start + end) / 2)

        if nums[mid] == k:
            return mid

        elif nums[mid] > k:
            end = mid - 1

        elif nums[mid] < k:
            start = mid + 1

    return 'Not found'


def binarySearchRecur(nums, start, end, k):
    if start >= end:
        return 'Not Found'

    mid = int((start + end) / 2)
    if nums[mid] == k:
        return mid

    elif nums[mid] > k:
        return binarySearchRecur(nums, start, mid - 1, k)

    elif nums[mid] < k:
        return binarySearchRecur(nums, mid + 1, end, k)


nums = [1, 2, 3, 4, 5]
k = 2
print(binarySearch(nums, k))
# print(binarySearchRecur(nums, 0, len(nums), k))
