class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        ans = ''

        for idx in range(len(s)):
            ans += s[indices.index(idx)]
        return ans

