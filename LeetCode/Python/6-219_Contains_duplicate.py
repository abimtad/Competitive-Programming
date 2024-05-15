class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        twins = {}
        for idx, num in enumerate(nums):
            if num in twins and abs(idx - twins[num]) <= k:
                return True
            twins[num] = idx
        else:
            return False
