class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        result = ""
        for x in words:
            result += x[::-1] + " "
        return result.rstrip()
