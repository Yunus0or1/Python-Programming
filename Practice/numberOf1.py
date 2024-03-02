class Solution:
    def hammingWeight(self, n: int) -> int:
        decimel = 0
        base = 1
        count = 0

        while n != 0:
            rem = n % 10
            n = int(n / 10)
            decimel = decimel + base * rem
            base = base * 2
            if rem == 1:
                count = count + 1

        return count

n = 101
s = Solution()
print(s.hammingWeight(n))