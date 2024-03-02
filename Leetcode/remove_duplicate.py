from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1

        i  = 0
        j = 0

        for i in range (0, len(nums)):
            if i == j:
                continue

            if nums[i] != nums[j]:
                j= i
                continue

            if nums[i] == nums[j]:
                nums[i] = -101

        j = 0
        for i in range (1, len(nums)):
            if nums[i] == -101 and j == 0:
                j = i
                continue

            if nums[i] != -101:
                nums[i],nums[j] = nums[j], nums[i]
                nums[i] = -101
                j = j + 1

        return j




p1 = Solution()
print(p1.removeDuplicates(nums=[1,1,1,2,2]))

[1,  1,    1,   2,  2]
[1, -101, -101, 2, -101]
