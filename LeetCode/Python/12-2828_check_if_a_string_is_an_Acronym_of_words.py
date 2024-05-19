class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        if len(words) != len(s):
            return False
        return all(map(lambda word, abbr: word[0] == abbr, words, s))
