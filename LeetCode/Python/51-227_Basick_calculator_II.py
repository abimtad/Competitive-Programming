class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        current_number = 0
        operation = '+'
        s = s.replace(' ', '')
        
        for i, char in enumerate(s):
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            
            if char in '+-*/' or i == len(s) - 1:
                if operation == '+':
                    stack.append(current_number)
                elif operation == '-':
                    stack.append(-current_number)
                elif operation == '*':
                    stack.append(stack.pop() * current_number)
                elif operation == '/':
                    last = stack.pop()
                    if last < 0:
                        stack.append(-(-last // current_number))
                    else:
                        stack.append(last // current_number)
                
                operation = char
                current_number = 0
        
        return sum(stack)
