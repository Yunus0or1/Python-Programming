def heapify(nums,n, currentIndex):

    largest = currentIndex
    left = 2 * currentIndex + 1
    right = 2 * currentIndex + 2

    if left<n and nums[left] > nums[largest]:
        largest = left
    if right<n and nums[right] > nums[largest]:
        largest = right

    if largest!= currentIndex:
        nums[largest], nums[currentIndex] = nums[currentIndex], nums[largest]
        heapify(nums,n, largest)



def heapSort(nums):
    n = len(nums)

    for i in range(n//2, -1, -1):
        heapify(nums,n, i )

    for i in range(n-1, -1, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, i , 0)


nums = [ 3, 9, 8, 7,1,1,8]
heapSort(nums)
print(nums)
