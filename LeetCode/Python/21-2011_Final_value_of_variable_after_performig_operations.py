class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        values = {"--X": -1, "X--": -1, "X++": 1, "++X": 1}
        X = 0

        for operation in operations:
            X += values[operation]

        return X

