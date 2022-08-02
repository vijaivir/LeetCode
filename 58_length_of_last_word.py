class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp = s.split()
        return len(temp[len(temp) - 1])
