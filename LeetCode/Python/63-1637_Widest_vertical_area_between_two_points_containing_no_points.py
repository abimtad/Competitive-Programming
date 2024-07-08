class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        x_coords = [point[0] for point in points]
    
        x_coords.sort()
    
        max_width = 0
    
        for i in range(1, len(x_coords)):
            max_width = max(max_width, x_coords[i] - x_coords[i-1])
    
        return max_width
