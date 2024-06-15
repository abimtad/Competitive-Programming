class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        breaks = 0
        
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                breaks += 1
        
        return breaks <= 1


