# Credit @Nikhilcode123 from Leetcode Discussions

class Solution:
    def myAtoi(self, s: str) -> int:
        ptr = 0
        size = len(s)
        result = 0
        sign = 1
        while ptr < size and s[ptr] == ' ':
            ptr += 1
        if ptr < size and s[ptr] == '-':
            sign = -1
            ptr += 1
        elif ptr < size and s[ptr] == '+':
            ptr += 1
        while ptr < size and s[ptr].isdigit():
            result = result * 10 + int(s[ptr])
            ptr += 1
        result *= sign
        MAX = 2 ** 31 - 1
        MIN = -2 ** 31
        if result > (2**31) - 1:
            return MAX
        if result < (-2**31):
            return MIN
        return result
