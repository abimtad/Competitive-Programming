class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = 0
        result = []

        for char in s:
            if char == '(':
                if count > 0:
                    result.append(char)
                count += 1
            elif char == ')':
                count -= 1
                if count > 0:
                    result.append(char)

        return ''.join(result)