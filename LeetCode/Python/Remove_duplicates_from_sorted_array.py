class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 0
        while idx < len(nums) - 1:
            if nums[idx] == nums[idx + 1]:
                del nums[idx + 1]
            else:
                idx += 1
        return len(nums)