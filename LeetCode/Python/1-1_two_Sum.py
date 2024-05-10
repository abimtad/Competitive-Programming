"""Solution to twoSum array problem. This is my fist leetCode problem. its indeed a brute force solution"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        operand_idxes = []
        length = len(nums)
        for first_idx in range(length - 1):
            for second_idx in range(first_idx + 1, length):
                _sum = nums[first_idx] + nums[second_idx]
                if _sum == target:
                    operand_idxes.extend([first_idx, second_idx])
                    break
        return operand_idxes