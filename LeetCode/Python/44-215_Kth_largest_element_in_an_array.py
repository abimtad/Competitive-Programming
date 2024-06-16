class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
       
        count = 1
        while count < k:
            nums.remove(max(nums))
            count += 1
        return max(nums)
        # return sorted(nums, reverse=True)[k - 1]
        
