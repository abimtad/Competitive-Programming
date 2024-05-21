class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = [lower(char) for char in s if char.isalnum()]

        return string == string[::-1]
