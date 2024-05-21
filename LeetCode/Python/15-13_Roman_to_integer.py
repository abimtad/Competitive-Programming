class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_numerals = {
                            'I': 1, 'V': 5, 'X': 10, 'L': 50,
                            'C': 100, 'D': 500, 'M': 1000
                        }
        arabic_numeral = digit = 0

        for idx in range(len(s)):
            digit = roman_numerals[s[idx]]
            if (idx != len(s) - 1) and (roman_numerals[s[idx]] < roman_numerals[s[idx + 1]]):
                digit *= -1
            arabic_numeral += digit
        
        return arabic_numeral
        