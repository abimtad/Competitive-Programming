class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False
        
        for idx in range(len(arr) - 2):
            if arr[idx] & 1 != 0 and arr[idx + 1] & 1 != 0 and arr[idx + 2] & 1 != 0:
                return True
        
        return False

