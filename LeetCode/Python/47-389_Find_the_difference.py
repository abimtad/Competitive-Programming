class Solution(object):
    def findTheDiference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        result = 0
    
        for char in s:
            result ^= ord(char)
        
        for char in t:
            result ^= ord(char)
        
        return chr(result)f
