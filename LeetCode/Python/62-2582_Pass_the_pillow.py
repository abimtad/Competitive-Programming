class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        position = 1
        direction = 1
        
        for _ in range(time):
            position += direction
            
            if position == n:  
                direction = -1
            elif position == 1:
                direction = 1
        
        return position 
            