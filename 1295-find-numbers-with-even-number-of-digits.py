class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for number in nums:
            if number < 10:
                pass
            elif number >= 10 and number < 100:
                count += 1
            elif number >= 100 and number < 1000:
                pass
            elif number >= 1000 and number < 10000:
                count += 1
            elif number >= 10000 and number < 100000:
                pass
            elif number >= 100000 and number < 1000000:
                count += 1
        return count
