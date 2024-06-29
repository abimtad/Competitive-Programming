class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        ones_count = s.count('1')
        zeros_count = s.count('0')
        
        result = '1' * (ones_count - 1) + '0' * zeros_count + '1'
        
        return result
