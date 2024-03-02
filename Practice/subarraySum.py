# class Solution(object):
#     def subarraySum(self, nums, k):
#         dict = {}
#         total = 0
#
#         for i in range(len(nums)):
#             sum = nums[i]
#
#             if sum == k:
#                 total = total + 1
#
#             for j in range(i + 1, len(nums)):
#                 sum = sum + nums[j]
#
#                 if sum == k:
#                     total = total + 1
#
#         return total

class Solution(object):
    def subarraySum(self, nums, k):
        dict = {}
        total = 0
        sum = 0

        for i in range(len(nums)):
            sum = sum + nums[i]

            dict[i] = sum

        return dict

nums = [1,2,3,-3,5]
k = 3

s = Solution()
print(s.subarraySum(nums,k))