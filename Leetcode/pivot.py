class Solution:
    def pivotInteger(self, n: int) -> int:
        totalSum = (n * (n+1) //2)
        for x in range(n, n // 2, -1):
            left = x * (x + 1) // 2
            right = totalSum - left + x

            print(left,right, x)

            if left == right:
                return x

        return -1


p1 = Solution()
print(p1.pivotInteger(n=0))
