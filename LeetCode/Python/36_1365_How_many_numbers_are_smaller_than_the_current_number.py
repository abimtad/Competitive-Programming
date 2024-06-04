class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hash_table = {}
        sorted_nums = sorted(nums)

        for idx, num in enumerate(sorted_nums):
            if num not in hash_table:
                hash_table[num] = idx
         
        return [hash_table[num] for num in nums]

