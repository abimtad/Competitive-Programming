class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s_list = s.split()
        truncted = ' '.join(s_list[:k])
        return truncted