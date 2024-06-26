class Solution:
   def isValid(self, s):
        stack = []
        stack_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in stack_map:
                if not stack:
                    return False
                top_element = stack.pop()
                if stack_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack
