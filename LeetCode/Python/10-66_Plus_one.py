class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int("".join(map(str, digits)))
        num += 1
        result = list(map(int, str(num)))
        
        return result
