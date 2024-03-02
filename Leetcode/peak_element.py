from typing import List


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        result = []

        for i in range(0, len(mountain) - 1):
            if i == 0:
                continue

            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                result.append(i)

        return result


p1 = Solution()
print(p1.findPeaks(mountain=[1,1,2]))
