class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch not in word:
            return word
        else:
            return word[:word.index(ch) + 1][::-1] + word[word.index(ch) + 1:]

