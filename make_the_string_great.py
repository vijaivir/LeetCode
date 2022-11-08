class Solution:
    def makeGood(self, s: str) -> str:
        for x in range(len(s) - 1):
            if abs(ord(s[x]) - ord(s[x+1])) == 32:
                return self.makeGood(s[:x] + s[x+2:])
        return s
