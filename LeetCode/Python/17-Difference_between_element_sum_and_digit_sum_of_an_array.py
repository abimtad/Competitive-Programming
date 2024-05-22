class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_1 = sum(nums)
        sum_2 = 0
        for num in nums:
            divisor = num
            while divisor > 0:
                sum_2 += divisor % 10
                divisor /= 10
        return abs(sum_1 - sum_2)
