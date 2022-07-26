"""
 My solution works by simply traversing the roman numeral string
 and adding 1, 5, 10, 50, 100, 500, 1000 corresponding to 
 'I', 'V', 'X', 'L', 'C', 'D', 'M' respectively. The 6 instances
 when 'I' is placed before 'V' or 'X', 'X' is placed before 'L' 
 or 'C', and 'C' is placed before 'D' or 'M', the algorithm subtracts
 the corresponding integer. 
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        integer = 0
        for x in range(0, len(s)):
            if s[x] == 'I':
                if len(s) - 1 > x and (s[x+1] == 'V' or s[x+1] == 'X'):
                    integer -= 1
                else:
                    integer += 1
            if s[x] == 'V':
                integer += 5
            if s[x] == 'X':
                if len(s) - 1 > x and (s[x+1] == 'L' or s[x+1] == 'C'):
                    integer -= 10
                else:
                    integer += 10
            if s[x] == 'L':
                integer += 50
            if s[x] == 'C':
                if len(s) - 1 > x and (s[x+1] == 'D' or s[x+1] == 'M'):
                    integer -= 100
                else:
                    integer += 100
            if s[x] == 'D':
                integer += 500
            if s[x] == 'M':
                integer += 1000                
        return integer