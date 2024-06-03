class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        arr = []
        while nums:
            alice_min = nums.pop(0)
            bob_min = nums.pop(0)
            arr.extend([bob_min, alice_min])
        
        return arr

