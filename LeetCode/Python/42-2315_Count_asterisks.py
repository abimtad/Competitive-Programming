inside_pair = False
        count = 0

        for char in s:
            if char == '|':
                inside_pair = not inside_pair
            elif char == '*' and not inside_pair:
                count += 1
        
        return count

