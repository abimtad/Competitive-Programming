class Solution(object):
        def isPowerOfTwo(self,n,i=0):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (n - 1)) == 0

