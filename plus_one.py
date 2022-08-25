class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = ''
        for x in range(len(digits)):
            result += str(digits[x])
        result = str(int(result) + 1)
        return list(result)
