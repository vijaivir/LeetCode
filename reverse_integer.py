class Solution:
    def reverse(self, x: int) -> int:
        # Reverse the string
        result = str(x)[::-1]
        # If the string contains '-', remove it and 
        # place it at beggining of the string
        if result[len(result) - 1] == '-':
            result = result[:-1]
            result = '-' + result
        # Convert to int to remove any '0' chars
        result = int(result)
        # Check 32-bit int constraints and return string
        if (-2 ** 31) <= result <= (2 ** 31) - 1:
            return str(result)
        return 0
