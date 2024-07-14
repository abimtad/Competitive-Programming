class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        n = len(rings) // 2
        rods = {str(i): set() for i in range(10)}
        
        for i in range(n):
            color = rings[2*i]
            rod = rings[2*i + 1]
            rods[rod].add(color)
        
        count = 0
        for rod in rods:
            if len(rods[rod]) == 3:
                count += 1
        
        return count
