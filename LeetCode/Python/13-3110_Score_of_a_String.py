class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        score, length = 0, len(s)

        for char_idx in range(length - 1):
            score += abs(ord(s[char_idx]) - ord(s[char_idx + 1]))
        
        return score
