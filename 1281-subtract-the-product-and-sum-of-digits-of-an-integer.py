class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        digitSum = 0
        index = 0
        for charector in str(n):
            digit = str(n)[index]
            index += 1
            digitSum += int(digit)
            product = product * int(digit)
                
        return product - digitSum

