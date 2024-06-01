class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        resored  = ''

        for idx in range(len(s)):
            resored += s[indices.index(idx)]
        return resored

