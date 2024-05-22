class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        sum = 0

        for letter in s:
            sum += abs(s.index(letter) - t.index(letter))
        
        return sum
