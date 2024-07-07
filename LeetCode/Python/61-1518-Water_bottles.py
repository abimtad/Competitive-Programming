class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
            """
        total_drinks = 0
        numEmpty = 0
        
        while numBottles > 0:
            total_drinks += numBottles
            numEmpty += numBottles
            numBottles = numEmpty // numExchange
            numEmpty = numEmpty % numExchange
        
        return total_drinks
            