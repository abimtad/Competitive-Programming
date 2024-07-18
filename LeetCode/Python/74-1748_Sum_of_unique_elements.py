class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_dict = {}
    
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        
        unique_sum = 0
        for num, count in count_dict.items():
            if count == 1:
                unique_sum += num
        
        return unique_sum
