class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n
        stairs = 1

        while left <= right:
            mid = left +  (right - left) //2
            totalCoinsNeed = mid * (mid + 1) // 2

            if totalCoinsNeed > n:
                right = mid -1
            else :
                stairs = max(stairs, mid)
                left = mid + 1

        return stairs



p1 = Solution()
print(p1.arrangeCoins(n=1))
