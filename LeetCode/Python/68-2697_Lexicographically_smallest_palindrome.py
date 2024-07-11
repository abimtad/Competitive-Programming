class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        n = len(s)
        
        for i in range(n // 2):
            j = n - i - 1  
            
            if s[i] != s[j]:
                if s[i] < s[j]:
                    s[j] = s[i]
                else:
                    s[i] = s[j]
        
        return ''.join(s)
            