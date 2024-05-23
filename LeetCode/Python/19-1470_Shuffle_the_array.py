class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        idx_1 = 0
        idx_2 = n
        ans = []

        while idx_2 <= len(nums) - 1:
            ans.extend([nums[idx_1], nums[idx_2]])

            idx_1 += 1
            idx_2 += 1
        
        return ans

