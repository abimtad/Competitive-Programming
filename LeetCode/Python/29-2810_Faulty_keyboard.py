class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""

        for char in s:
            if char == 'i':
                ans = ans[::-1]
            else:
                ans += char

        return ans

