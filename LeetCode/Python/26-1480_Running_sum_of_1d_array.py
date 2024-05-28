class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for idx in range(len(nums)):
            if idx == 0:
                continue
            nums[idx] = sum(nums[idx - 1:idx + 1])
            
        return nums
