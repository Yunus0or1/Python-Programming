class Solution(object):
    def getMedian(self, nums, k):
        nums = sorted(nums)

        if k%2 == 1:
            median = nums[int(len(nums) / 2)]

        if k % 2 == 0:
            median = (nums[int(len(nums) / 2) - 1] + nums[int(len(nums) / 2)]) / 2

        return median

    def medianSlidingWindow(self, nums, k):
        result = []
        for i in range(len(nums) - k + 1):
            current = nums[i:i+k]
            result.append(self.getMedian(current,k))
        return result



# nums = [1,2,3,4,2,3,1,4,2]
# k = 3

nums = [1,4,2,3]
k = 4
s = Solution()

print(s.medianSlidingWindow(nums,k))