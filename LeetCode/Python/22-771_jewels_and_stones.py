class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        num_jewels = 0

        for jewel in jewels:
            num_jewels += stones.count(jewel)
        
        return num_jewels

