class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        total_min_mvs = 0  

        for i in range(len(seats)):
            total_min_mvs += abs(seats[i] - students[i])

        return total_min_mvs

