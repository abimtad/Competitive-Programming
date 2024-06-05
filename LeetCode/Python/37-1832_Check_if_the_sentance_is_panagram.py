class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        unique_letters = set()

        for char in sentence:
            unique_letters.add(char)
            
        return len(unique_letters) == 26
    
